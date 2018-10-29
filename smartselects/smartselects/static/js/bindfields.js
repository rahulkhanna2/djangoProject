(function ($) {
    "use strict";
	
	chainedfk = function() {
        return {
            fireEvent: function (element, event) {
                var evt, rtn;
                if (document.createEventObject) {
                    // dispatch for IE
                    evt = document.createEventObject();
                    rtn = element.fireEvent('on' + event, evt);
                } else {
                    // dispatch for firefox + others
                    evt = document.createEvent("HTMLEvents");
                    evt.initEvent(event, true, true); // event type,bubbling,cancelable
                    rtn = !element.dispatchEvent(evt);
                }

                return rtn;
            },
            dismissRelatedLookupPopup: function (win, chosenId) {
                var name = windowname_to_id(win.name),
                    elem = document.getElementById(name);
                if (elem.className.indexOf('vManyToManyRawIdAdminField') !== -1 && elem.value) {
                    elem.value += ',' + chosenId;
                } else {
                    elem.value = chosenId;
                }
                fireEvent(elem, 'change');
                win.close();
            },
            fill_field: function (val, init_value, elem_id, url, empty_label, auto_choose) {
                var $selectField = $(elem_id),
                    options = [];
                url = url + "/" + val + "/";

                var empty_option =  $('<option></option>')
                    .attr('value', '')
                    .text(empty_label);

                if (!val || val === '') {
                    empty_option.prop('selected', true);
                    options.push(empty_option);

                    $selectField.html(options);
                    $selectField.trigger('change');
                    return;
                }
                $.getJSON(url, function (j) {
                    auto_choose = j.length === 1 && auto_choose;
                    // Append empty label as the first option
                    if (!(init_value || auto_choose)) {
                        empty_option.prop('selected', true);
                    }
                    options.push(empty_option);

                    // Append each option to the select
                    $.each(j, function (index, optionData) {
                        var option = $('<option></option>')
                            .prop('value', optionData.value)
                            .text(optionData.display);
                        if (auto_choose === "true" || auto_choose === "True") {
                            auto_choose = true;
                        } else if (auto_choose === "false" || auto_choose === "False") {
                            auto_choose = false;
                        }
                        if (auto_choose || (init_value && optionData.value === init_value)) {
                            option.prop('selected', true);
                        }
                        options.push(option);
                    });

                    $selectField.html(options);
                    var width = $selectField.outerWidth();
                    if (navigator.appVersion.indexOf("MSIE") !== -1) {
                        $selectField.width(width + 'px');
                    }

                    $selectField.trigger('change');
                });
            },
            init: function (chainfield, url, id, init_value, empty_label, auto_choose) {
                var val, fill_field = this.fill_field;

                if (!$(chainfield).hasClass("chained")) {
                    val = $(chainfield).val();
                    fill_field(val, init_value, id, url, empty_label, auto_choose);
                }
                $(chainfield).change(function () {
                    // Handle the case of inlines, where the ID will depend on which list item we are dealing with
                    var prefix, start_value, this_val, localID = id;
                    if (localID.indexOf("__prefix__") > -1) {
                        prefix = $(this).attr("id").match(/\d+/)[0];
                        localID = localID.replace("__prefix__", prefix);
                    }

                    start_value = $(localID).val();
                    this_val = $(this).val();
                    fill_field(this_val, start_value, localID, url, empty_label, auto_choose);
                });
                if (typeof(dismissAddAnotherPopup) !== 'undefined') {
                    var oldDismissAddAnotherPopup = dismissAddAnotherPopup;
                    dismissAddAnotherPopup = function (win, newId, newRepr) {
                        oldDismissAddAnotherPopup(win, newId, newRepr);
                        if (windowname_to_id(win.name) === chainfield) {
                            $(chainfield).change();
                        }
                    };
                }
            }
        };
    }();
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	

    function initItem(item) {
        var empty_label, chainfield = "#id_" + $(item).attr("data-chainfield"),
            url = $(item).attr("data-url"),
            id = "#" + $(item).attr("id"),
            value = JSON.parse($(item).attr("data-value")),
            auto_choose = $(item).attr("data-auto_choose");
        if ($(item).hasClass("chained-fk")) {
            empty_label = $(item).attr("data-empty_label");
            chainedfk.init(chainfield, url, id, value, empty_label, auto_choose);
        } else if ($(item).hasClass("chained")) {
            chainedm2m.init(chainfield, url, id, value, auto_choose);
        } else if ($(item).hasClass("filtered")) {
            // For the ManyToMany using horizontal=True added after the page load
            // using javascript.
            id = id.replace('_from', ''); // we need to remove the _from part
            chainedm2m.init(chainfield, url, id, value, auto_choose);
        }
    }

    $(window).on('load', function () {
        $.each($(".chained"), function (index, item) {
            initItem(item);
        });
    });

    $(document).ready(function () {
        $.each($(".chained-fk"), function (index, item) {
            initItem(item);
        });
    });

    function initFormset(chained) {
        var re = /\d+/g,
            prefix,
            match,
            chainfield = $(chained).attr("data-chainfield"),
            chainedId = $(chained).attr("id");
        if (chainfield.indexOf("__prefix__") > -1) {
            /*
             If we have several inlines with the same name, they will get an index, so we need to ignore that and get
             the last numeric value in the id
             */
            do {
                match = re.exec(chainedId);
                if (match) {
                    prefix = match[0];
                }
            } while (match);

            chainfield = chainfield.replace("__prefix__", prefix);
            $(chained).attr("data-chainfield", chainfield);
        }
        initItem(chained);
    }

    $(document).on('formset:added', function (event, $row, formsetName) {
        // Fired every time a new inline formset is created

        var chainedFK, chainedM2M, filteredM2M;

        // For the ForeingKey
        chainedFK = $row.find(".chained-fk");
        $.each(chainedFK, function (index, chained) {
            initFormset(chained);
        });

        // For the ManyToMany
        chainedM2M = $row.find(".chained");
        $.each(chainedM2M, function (index, chained) {
            initFormset(chained);
        });

        // For the ManyToMany using horizontal=True added after the page load
        // using javascript.
        filteredM2M = $row.find(".filtered");
        $.each(filteredM2M, function (index, filtered) {
            if (filtered.hasAttribute('data-chainfield')) {
                initFormset(filtered);
            }
        });
    });
}(jQuery || django.jQuery));
