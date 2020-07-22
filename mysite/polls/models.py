# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from smart_selects.db_fields import ChainedForeignKey



class AppAuthentication(models.Model):
    app_id = models.CharField(max_length=255)
    app_secret = models.CharField(max_length=255)
    endpoint_name = models.CharField(max_length=255, blank=True, null=True)
    source_ip = models.CharField(max_length=255, blank=True, null=True)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'app_authentication'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BlockedDealsRewards(models.Model):
    blocked_deals_id = models.CharField(primary_key=True, max_length=254)
    user = models.ForeignKey('UserTable', models.DO_NOTHING)
    blocked_till_date_time = models.DateTimeField(blank=True, null=True)
    unsuccessful_attempt_count = models.IntegerField()
    last_pin_attempt_date_time = models.DateTimeField()
    deal = models.ForeignKey('DealsMain', models.DO_NOTHING)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'blocked_deals_rewards'


class BlockedMerchantPin(models.Model):
    blocked_pin_id = models.CharField(primary_key=True, max_length=254)
    user = models.ForeignKey('UserTable', models.DO_NOTHING)
    blocked_till_date_time = models.DateTimeField(blank=True, null=True)
    unsuccessful_attempt_count = models.IntegerField(blank=True, null=True)
    last_pin_attempt_date_time = models.DateTimeField(blank=True, null=True)
    merchant = models.ForeignKey('MerchantMain', models.DO_NOTHING)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'blocked_merchant_pin'


class BlockedStampsRewards(models.Model):
    blocked_stamps_id = models.CharField(primary_key=True, max_length=45)
    user = models.ForeignKey('UserTable', models.DO_NOTHING)
    blocked_till_date_time = models.DateTimeField(blank=True, null=True)
    unsuccessful_attempt_count = models.IntegerField(blank=True, null=True)
    last_pin_attempt_date_time = models.DateTimeField(blank=True, null=True)
    stamp_card = models.ForeignKey('StampCardsMain', models.DO_NOTHING, blank=True, null=True)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'blocked_stamps_rewards'


class CollectionAudit(models.Model):
    audit_id = models.AutoField(primary_key=True)
    collection_id = models.IntegerField()
    title = models.CharField(max_length=50)
    sub_title = models.CharField(max_length=100)
    publish_date = models.DateTimeField()
    collection_type = models.IntegerField()
    creation_time = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    small_img_url = models.CharField(max_length=250)
    is_header = models.IntegerField()
    header_title = models.CharField(max_length=50, blank=True, null=True)
    header_subtitle = models.CharField(max_length=100, blank=True, null=True)
    header_img_url = models.CharField(max_length=250, blank=True, null=True)
    header_small_img_url = models.CharField(max_length=250, blank=True, null=True)
    header_publish_date = models.DateTimeField(blank=True, null=True)
    header_expiry_date = models.DateTimeField(blank=True, null=True)
    banner_img_url = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collection_audit'


class CollectionsMain(models.Model):
    collection_id = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=50)
    sub_title = models.CharField(max_length=100)
    publish_date = models.DateTimeField()
    collection_type = models.IntegerField()
    creation_time = models.DateTimeField()
    updated_at = models.DateTimeField()
    status = models.IntegerField()
    small_img_url = models.CharField(max_length=2000)
    is_header = models.IntegerField()
    header_title = models.CharField(max_length=50, blank=True, null=True)
    header_subtitle = models.CharField(max_length=100, blank=True, null=True)
    header_img_url = models.CharField(max_length=2000, blank=True, null=True)
    header_small_img_url = models.CharField(max_length=2000, blank=True, null=True)
    header_publish_date = models.DateTimeField(blank=True, null=True)
    header_expiry_date = models.DateTimeField(blank=True, null=True)
    banner_img_url = models.CharField(max_length=2000, blank=True, null=True)
    filter_icon_url = models.CharField(max_length=2000)
    is_filtering_allowed = models.IntegerField(blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'collections_main'


class DealCouponCodes(models.Model):
    coupon_code_id = models.AutoField(primary_key=True)
    deal = models.ForeignKey('DealsMain', models.DO_NOTHING)
    coupon_code = models.CharField(max_length=2000)
    is_used = models.IntegerField()
    created_date = models.DateTimeField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deal_coupon_codes'


class DealsAudit(models.Model):
    audit_id = models.AutoField(primary_key=True)
    deal_id = models.IntegerField()
    title = models.CharField(max_length=45, blank=True, null=True)
    sub_title = models.CharField(max_length=45, blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)
    merchant_id = models.IntegerField(blank=True, null=True)
    tnc = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    last_updated_at = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    provided_inventory = models.IntegerField(blank=True, null=True)
    total_inventory = models.IntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    small_img_url = models.CharField(max_length=250, blank=True, null=True)
    big_img_url = models.CharField(max_length=250)
    is_header = models.IntegerField()
    header_title = models.CharField(max_length=50, blank=True, null=True)
    header_subtitle = models.CharField(max_length=100, blank=True, null=True)
    header_img_url = models.CharField(max_length=250, blank=True, null=True)
    header_publish_date = models.DateTimeField(blank=True, null=True)
    header_expiry_date = models.DateTimeField(blank=True, null=True)
    deal_type = models.IntegerField()
    promocode = models.CharField(max_length=10, blank=True, null=True)
    is_locked = models.IntegerField()
    marketing_event_name = models.CharField(max_length=70, blank=True, null=True)
    max_redemption_count = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'deals_audit'




class DealsMain(models.Model):
    deal_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)
    merchant = models.ForeignKey('MerchantMain', models.DO_NOTHING, blank=True, null=True)
    tnc = models.CharField(max_length=5000)
    start_date = models.DateTimeField(blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    last_updated_at = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    provided_inventory = models.IntegerField(blank=True, null=True)
    total_inventory = models.IntegerField()
    end_date = models.DateTimeField(blank=True, null=True)
    small_img_url = models.CharField(max_length=2000, blank=True, null=True)
    big_img_url = models.CharField(max_length=2000)
    is_header = models.IntegerField()
    header_title = models.CharField(max_length=50, blank=True, null=True)
    header_subtitle = models.CharField(max_length=100, blank=True, null=True)
    header_img_url = models.CharField(max_length=250, blank=True, null=True)
    header_publish_date = models.DateTimeField(blank=True, null=True)
    header_expiry_date = models.DateTimeField(blank=True, null=True)
    deal_type = models.IntegerField()
    promocode = models.CharField(max_length=2000, blank=True, null=True)
    is_locked = models.IntegerField()
    marketing_event_name = models.CharField(max_length=70, blank=True, null=True)
    max_redemption_count = models.IntegerField()
    percentage_disc = models.IntegerField()
    dollar_disc = models.IntegerField()
    min_basket_value = models.IntegerField()
    max_discount_amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'deals_main'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DealsCollections(models.Model):
    deal = ChainedForeignKey('Deals')
    deal = models.ForeignKey('DealsMain', models.DO_NOTHING, blank=True, null=True)
    collection = models.ForeignKey(CollectionsMain, models.DO_NOTHING, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deals_collections'


class MerchantCollections(models.Model):
    deal = models.ForeignKey(DealsCollections, on_delete=models.CASCADE)
    collection = models.ForeignKey(CollectionsMain, models.DO_NOTHING)
    merchant = models.ForeignKey('MerchantMain', models.DO_NOTHING, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_collections'


class MerchantMain(models.Model):
    merchant_id = models.AutoField(primary_key=True)
    merchant_name = models.CharField(max_length=45, blank=True, null=True)
    subtitle = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    our_story = models.CharField(max_length=2000, blank=True, null=True)
    creation_time = models.DateTimeField()
    last_updated_at = models.DateTimeField()
    small_img_url = models.CharField(max_length=2000, blank=True, null=True)
    big_img_url = models.CharField(max_length=2000, blank=True, null=True)
    is_header = models.IntegerField()
    header_title = models.CharField(max_length=50, blank=True, null=True)
    header_subtitle = models.CharField(max_length=100, blank=True, null=True)
    header_img_url = models.CharField(max_length=2000, blank=True, null=True)
    header_publish_date = models.DateTimeField(blank=True, null=True)
    header_expiry_date = models.DateTimeField(blank=True, null=True)
    issuance_rate_linkpoint = models.IntegerField()
    issuance_rate_dollar_value = models.IntegerField()
    description = models.CharField(max_length=5000, blank=True, null=True)
    web_url = models.CharField(max_length=2000, blank=True, null=True)
    tnc = models.CharField(max_length=5000, blank=True, null=True)
    echoss_merchant_id = models.CharField(max_length=45, blank=True, null=True)
    is_cls_merchant = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_main'


class MerchantSpoc(models.Model):
    spoc_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45, blank=True, null=True)
    store = models.ForeignKey('MerchantStores', models.DO_NOTHING)
    mobile_number = models.CharField(max_length=10)
    email_addr = models.CharField(max_length=100)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'merchant_spoc'


class MerchantStores(models.Model):
    store_id = models.AutoField(primary_key=True)
    merchant = models.ForeignKey(MerchantMain, models.DO_NOTHING, blank=True, null=True)
    geox = models.CharField(db_column='geoX', max_length=45, blank=True, null=True)  # Field name made lowercase.
    geoy = models.CharField(db_column='geoY', max_length=45, blank=True, null=True)  # Field name made lowercase.
    store_name = models.CharField(max_length=70)
    address_line1 = models.CharField(max_length=70, blank=True, null=True)
    address_line2 = models.CharField(max_length=70, blank=True, null=True)
    postal_code = models.CharField(max_length=45, blank=True, null=True)
    sms_opt_in = models.IntegerField(blank=True, null=True)
    email_opt_in = models.IntegerField(blank=True, null=True)
    store_type = models.IntegerField()
    unit_number = models.CharField(max_length=45, blank=True, null=True)
    level = models.CharField(max_length=45, blank=True, null=True)
    pin = models.CharField(unique=True, max_length=45, blank=True, null=True)
    pin_sent_date = models.DateTimeField(blank=True, null=True)
    pin_delivery_schedule = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    echoss_store_id = models.CharField(max_length=45, blank=True, null=True)
    cls_operator_id = models.CharField(max_length=45, blank=True, null=True)
    cls_merchant_id = models.IntegerField(blank=True, null=True)
    cls_terminal_id = models.IntegerField(blank=True, null=True)
    cls_pin = models.IntegerField(blank=True, null=True)
    qr_code = models.CharField(unique=True, max_length=8, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchant_stores'


class MerchantsAudit(models.Model):
    audit_id = models.AutoField(primary_key=True)
    merchant_id = models.IntegerField()
    merchant_name = models.CharField(max_length=45, blank=True, null=True)
    subtitle = models.CharField(max_length=45, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    our_story = models.CharField(max_length=2000, blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    last_updated_at = models.DateTimeField(blank=True, null=True)
    small_img_url = models.CharField(max_length=250, blank=True, null=True)
    big_img_url = models.CharField(max_length=250, blank=True, null=True)
    is_header = models.IntegerField()
    header_title = models.CharField(max_length=50, blank=True, null=True)
    header_subtitle = models.CharField(max_length=100, blank=True, null=True)
    header_img_url = models.CharField(max_length=250, blank=True, null=True)
    header_publish_date = models.DateTimeField(blank=True, null=True)
    header_expiry_date = models.DateTimeField(blank=True, null=True)
    issuance_rate_linkpoint = models.IntegerField()
    issuance_rate_dollar_value = models.IntegerField()
    description = models.CharField(max_length=300, blank=True, null=True)
    web_url = models.CharField(max_length=250, blank=True, null=True)
    tnc = models.CharField(max_length=500, blank=True, null=True)
    echoss_merchant_id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'merchants_audit'


class PollsChoice(models.Model):
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField()
    question = models.ForeignKey('PollsQuestion', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'polls_choice'


class PollsQuestion(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'polls_question'


class PromotionsAudit(models.Model):
    audit_id = models.AutoField(primary_key=True)
    promotion_id = models.IntegerField()
    title = models.CharField(max_length=45, blank=True, null=True)
    sub_title = models.CharField(max_length=45, blank=True, null=True)
    merchant_id = models.IntegerField(blank=True, null=True)
    tnc = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    last_updated_at = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    small_img_url = models.CharField(max_length=250, blank=True, null=True)
    big_img_url = models.CharField(max_length=250)
    is_header = models.IntegerField()
    header_title = models.CharField(max_length=50, blank=True, null=True)
    header_subtitle = models.CharField(max_length=100, blank=True, null=True)
    header_img_url = models.CharField(max_length=250, blank=True, null=True)
    header_publish_date = models.DateTimeField(blank=True, null=True)
    header_expiry_date = models.DateTimeField(blank=True, null=True)
    promotion_type = models.IntegerField(blank=True, null=True)
    promotion_url = models.CharField(max_length=250, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promotions_audit'


class PromotionsCollections(models.Model):
    promotion = models.ForeignKey('PromotionsMain', models.DO_NOTHING, blank=True, null=True)
    collection = models.ForeignKey(CollectionsMain, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promotions_collections'


class PromotionsMain(models.Model):
    promotion_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    merchant = models.ForeignKey(MerchantMain, models.DO_NOTHING, blank=True, null=True)
    tnc = models.CharField(max_length=5000, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    last_updated_at = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    small_img_url = models.CharField(max_length=2000, blank=True, null=True)
    big_img_url = models.CharField(max_length=2000)
    is_header = models.IntegerField()
    header_title = models.CharField(max_length=50, blank=True, null=True)
    header_subtitle = models.CharField(max_length=100, blank=True, null=True)
    header_img_url = models.CharField(max_length=2000, blank=True, null=True)
    header_publish_date = models.DateTimeField(blank=True, null=True)
    header_expiry_date = models.DateTimeField(blank=True, null=True)
    promotion_type = models.IntegerField(blank=True, null=True)
    promotion_url = models.CharField(max_length=2000, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'promotions_main'


class RewardsDeals(models.Model):
    user = models.ForeignKey('UserTable', models.DO_NOTHING)
    deal = models.ForeignKey(DealsMain, models.DO_NOTHING)
    date_added = models.DateTimeField()
    status = models.IntegerField()
    updated_date = models.DateTimeField()
    coupon_code = models.ForeignKey(DealCouponCodes, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'rewards_deals'


class RewardsStamps(models.Model):
    user = models.ForeignKey('UserTable', models.DO_NOTHING)
    stamp_card = models.ForeignKey('StampCardsMain', models.DO_NOTHING)
    date_added = models.DateTimeField()
    total_stamps_on_card = models.IntegerField()
    stamp_status = models.IntegerField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'rewards_stamps'


class StampCardsAudit(models.Model):
    audit_id = models.AutoField(primary_key=True)
    stamp_card_id = models.IntegerField()
    title = models.CharField(max_length=45, blank=True, null=True)
    sub_title = models.CharField(max_length=45, blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)
    merchant_id = models.IntegerField(blank=True, null=True)
    tnc = models.CharField(max_length=200, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    last_updated_at = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=300, blank=True, null=True)
    provided_inventory = models.IntegerField(blank=True, null=True)
    total_inventory = models.IntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    max_visits_per_hour = models.IntegerField(blank=True, null=True)
    text_on_stamp = models.CharField(max_length=32, blank=True, null=True)
    small_img_url = models.CharField(max_length=250, blank=True, null=True)
    big_img_url = models.CharField(max_length=250)
    is_header = models.IntegerField()
    header_title = models.CharField(max_length=50, blank=True, null=True)
    header_subtitle = models.CharField(max_length=100, blank=True, null=True)
    header_img_url = models.CharField(max_length=250, blank=True, null=True)
    header_publish_date = models.DateTimeField(blank=True, null=True)
    header_expiry_date = models.DateTimeField(blank=True, null=True)
    goal_asset_url = models.CharField(max_length=250)
    milestone_text = models.CharField(max_length=250, blank=True, null=True)
    total_steps = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stamp_cards_audit'


class StampCardsCollections(models.Model):
    stamp_card = models.ForeignKey('StampCardsMain', models.DO_NOTHING, blank=True, null=True)
    collection = models.ForeignKey(CollectionsMain, models.DO_NOTHING, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stamp_cards_collections'


class StampCardsMain(models.Model):
    stamp_card_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50, blank=True, null=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    status_code = models.IntegerField(blank=True, null=True)
    merchant = models.ForeignKey(MerchantMain, models.DO_NOTHING, blank=True, null=True)
    tnc = models.CharField(max_length=5000, blank=True, null=True)
    start_date = models.DateTimeField(blank=True, null=True)
    creation_time = models.DateTimeField(blank=True, null=True)
    last_updated_at = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)
    provided_inventory = models.IntegerField(blank=True, null=True)
    total_inventory = models.IntegerField(blank=True, null=True)
    end_date = models.DateTimeField(blank=True, null=True)
    max_visits_per_hour = models.IntegerField(blank=True, null=True)
    text_on_stamp = models.CharField(max_length=32, blank=True, null=True)
    small_img_url = models.CharField(max_length=2000, blank=True, null=True)
    big_img_url = models.CharField(max_length=2000)
    is_header = models.IntegerField()
    header_title = models.CharField(max_length=50, blank=True, null=True)
    header_subtitle = models.CharField(max_length=100, blank=True, null=True)
    header_img_url = models.CharField(max_length=2000, blank=True, null=True)
    header_publish_date = models.DateTimeField(blank=True, null=True)
    header_expiry_date = models.DateTimeField(blank=True, null=True)
    goal_asset_url = models.CharField(max_length=2000)
    milestone_text = models.CharField(max_length=250, blank=True, null=True)
    total_steps = models.IntegerField()
    max_redemption_count = models.IntegerField()
    rank = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stamp_cards_main'


class StaticContentMain(models.Model):
    content_id = models.AutoField(primary_key=True)
    content_key = models.CharField(max_length=256, blank=True, null=True)
    content_value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'static_content_main'


class StoreEchossEstamps(models.Model):
    merchant_store = models.ForeignKey(MerchantStores, models.DO_NOTHING)
    echoss_estamp_id = models.CharField(unique=True, max_length=45)
    echoss_estamp_serial_no = models.CharField(max_length=45)
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'store_echoss_estamps'


class StoresAudit(models.Model):
    audit_id = models.AutoField(primary_key=True)
    store_id = models.IntegerField()
    merchant_id = models.IntegerField(blank=True, null=True)
    geox = models.CharField(db_column='geoX', max_length=45, blank=True, null=True)  # Field name made lowercase.
    geoy = models.CharField(db_column='geoY', max_length=45, blank=True, null=True)  # Field name made lowercase.
    store_name = models.CharField(max_length=70)
    address_line1 = models.CharField(max_length=70, blank=True, null=True)
    address_line2 = models.CharField(max_length=70, blank=True, null=True)
    postal_code = models.CharField(max_length=45, blank=True, null=True)
    sms_opt_in = models.IntegerField(blank=True, null=True)
    email_opt_in = models.IntegerField(blank=True, null=True)
    store_type = models.IntegerField()
    unit_number = models.CharField(max_length=45, blank=True, null=True)
    level = models.CharField(max_length=45, blank=True, null=True)
    pin = models.CharField(max_length=45, blank=True, null=True)
    pin_sent_date = models.DateTimeField(blank=True, null=True)
    pin_delivery_schedule = models.IntegerField()
    created_date = models.DateTimeField()
    updated_date = models.DateTimeField()
    echoss_store_id = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stores_audit'


class UserDealRecords(models.Model):
    user = models.ForeignKey('UserTable', models.DO_NOTHING)
    deals_record_id = models.AutoField(primary_key=True)
    deal = models.ForeignKey(DealsMain, models.DO_NOTHING)
    deal_time = models.DateTimeField()
    geox = models.CharField(db_column='geoX', max_length=45, blank=True, null=True)  # Field name made lowercase.
    geoy = models.CharField(db_column='geoY', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ip_addr = models.CharField(max_length=45, blank=True, null=True)
    merchant = models.ForeignKey(MerchantMain, models.DO_NOTHING)
    from_state = models.IntegerField()
    to_state = models.IntegerField()
    merchant_store = models.ForeignKey(MerchantStores, models.DO_NOTHING, blank=True, null=True)
    updated_date = models.DateTimeField()
    source = models.CharField(max_length=45, blank=True, null=True)
    success_status = models.IntegerField(blank=True, null=True)
    echoss_metadata = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_deal_records'


class UserStampingRecords(models.Model):
    stamps_record_id = models.AutoField(primary_key=True)
    user = models.ForeignKey('UserTable', models.DO_NOTHING)
    stamp_card = models.ForeignKey(StampCardsMain, models.DO_NOTHING)
    stamp_time = models.DateTimeField()
    geox = models.CharField(db_column='geoX', max_length=45, blank=True, null=True)  # Field name made lowercase.
    geoy = models.CharField(db_column='geoY', max_length=45, blank=True, null=True)  # Field name made lowercase.
    ip_addr = models.CharField(max_length=45, blank=True, null=True)
    merchant = models.ForeignKey(MerchantMain, models.DO_NOTHING)
    from_state = models.IntegerField()
    to_state = models.IntegerField()
    merchant_store = models.ForeignKey(MerchantStores, models.DO_NOTHING, blank=True, null=True)
    updated_date = models.DateTimeField()
    source = models.CharField(max_length=45, blank=True, null=True)
    success_status = models.IntegerField(blank=True, null=True)
    echoss_metadata = models.CharField(max_length=5000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_stamping_records'


class UserTable(models.Model):
    user_id = models.CharField(primary_key=True, max_length=45)
    creation_date = models.DateTimeField()
    aid = models.CharField(unique=True, max_length=200)
    crm_id = models.CharField(max_length=45)
    updated_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user_table'
