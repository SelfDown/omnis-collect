# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AttachmentInfo(models.Model):
    attachment_id = models.CharField(primary_key=True, max_length=100)
    attachment_path = models.CharField(max_length=1000)
    nginx_path = models.CharField(max_length=1000, blank=True, null=True)
    access_module = models.CharField(max_length=50, blank=True, null=True)
    operation_user = models.CharField(max_length=50, blank=True, null=True)
    operation_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attachment_info'


class AttendanceArchive(models.Model):
    attendance_archive_id = models.CharField(primary_key=True, max_length=50)
    ym = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    userno = models.CharField(max_length=20)
    work_location = models.CharField(max_length=20)
    corp_name = models.CharField(max_length=50, blank=True, null=True)
    user_statu = models.CharField(max_length=50, blank=True, null=True)
    lv1_dep = models.CharField(max_length=50, blank=True, null=True)
    lv2_dep = models.CharField(max_length=50, blank=True, null=True)
    lv3_dep = models.CharField(max_length=50, blank=True, null=True)
    should_attendance = models.IntegerField(blank=True, null=True)
    actual_attendance = models.IntegerField(blank=True, null=True)
    d1 = models.CharField(max_length=4, blank=True, null=True)
    d2 = models.CharField(max_length=4, blank=True, null=True)
    d3 = models.CharField(max_length=4, blank=True, null=True)
    d4 = models.CharField(max_length=4, blank=True, null=True)
    d5 = models.CharField(max_length=4, blank=True, null=True)
    d6 = models.CharField(max_length=4, blank=True, null=True)
    d7 = models.CharField(max_length=4, blank=True, null=True)
    d8 = models.CharField(max_length=4, blank=True, null=True)
    d9 = models.CharField(max_length=4, blank=True, null=True)
    d10 = models.CharField(max_length=4, blank=True, null=True)
    d11 = models.CharField(max_length=4, blank=True, null=True)
    d12 = models.CharField(max_length=4, blank=True, null=True)
    d13 = models.CharField(max_length=4, blank=True, null=True)
    d14 = models.CharField(max_length=4, blank=True, null=True)
    d15 = models.CharField(max_length=4, blank=True, null=True)
    d16 = models.CharField(max_length=4, blank=True, null=True)
    d17 = models.CharField(max_length=4, blank=True, null=True)
    d18 = models.CharField(max_length=4, blank=True, null=True)
    d19 = models.CharField(max_length=4, blank=True, null=True)
    d20 = models.CharField(max_length=4, blank=True, null=True)
    d21 = models.CharField(max_length=4, blank=True, null=True)
    d22 = models.CharField(max_length=4, blank=True, null=True)
    d23 = models.CharField(max_length=4, blank=True, null=True)
    d24 = models.CharField(max_length=4, blank=True, null=True)
    d25 = models.CharField(max_length=4, blank=True, null=True)
    d26 = models.CharField(max_length=4, blank=True, null=True)
    d27 = models.CharField(max_length=4, blank=True, null=True)
    d28 = models.CharField(max_length=4, blank=True, null=True)
    d29 = models.CharField(max_length=4, blank=True, null=True)
    d30 = models.CharField(max_length=4, blank=True, null=True)
    d31 = models.CharField(max_length=4, blank=True, null=True)
    sj = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    bj = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    tx = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    jb = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    cc = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    hj = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    nj = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    pcj = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    sangjia = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    cj = models.DecimalField(max_digits=6, decimal_places=1, blank=True, null=True)
    op_user = models.CharField(max_length=50, blank=True, null=True)
    op_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_archive'


class AttendanceArchiveDay(models.Model):
    attendance_archive_day_id = models.CharField(primary_key=True, max_length=50)
    attendance_archive_id = models.CharField(max_length=50)
    projectid = models.CharField(max_length=20, blank=True, null=True)
    attendance_type = models.CharField(max_length=20)
    days = models.FloatField()
    rest_days = models.FloatField(blank=True, null=True)
    workday = models.DateField()
    early_time = models.FloatField(blank=True, null=True)
    late_time = models.FloatField(blank=True, null=True)
    onduty_address = models.CharField(max_length=255, blank=True, null=True)
    offduty_address = models.CharField(max_length=255, blank=True, null=True)
    onduty_city_id = models.CharField(max_length=255, blank=True, null=True)
    offduty_city_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_archive_day'


class AttendanceArchiveMonth(models.Model):
    attendance_archive_id = models.CharField(primary_key=True, max_length=50)
    ym = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    userno = models.CharField(max_length=20)
    work_location = models.CharField(max_length=20, blank=True, null=True)
    corp_name = models.CharField(max_length=50, blank=True, null=True)
    user_statu = models.CharField(max_length=50, blank=True, null=True)
    lv1_dep = models.CharField(max_length=50, blank=True, null=True)
    lv2_dep = models.CharField(max_length=50, blank=True, null=True)
    lv3_dep = models.CharField(max_length=50, blank=True, null=True)
    should_attendance = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    actual_attendance = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    op_user = models.CharField(max_length=50, blank=True, null=True)
    op_time = models.DateTimeField(blank=True, null=True)
    early_time_sum = models.FloatField(blank=True, null=True)
    late_time_sum = models.FloatField(blank=True, null=True)
    sj_sum = models.FloatField(blank=True, null=True)
    bj_sum = models.FloatField(blank=True, null=True)
    que_sum = models.FloatField(blank=True, null=True)
    kg_sum = models.FloatField(blank=True, null=True)
    cj_sum = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_archive_month'


class AttendanceBaseinfo(models.Model):
    attendance_baseinfo_id = models.CharField(primary_key=True, max_length=50)
    work_date = models.DateField()
    user_id = models.CharField(max_length=80)
    onduty_check_time = models.CharField(max_length=255, blank=True, null=True)
    onduty_check_time_result = models.CharField(max_length=255, blank=True, null=True)
    onduty_check_addr = models.CharField(max_length=255, blank=True, null=True)
    onduty_check_addr_result = models.CharField(max_length=255, blank=True, null=True)
    offduty_check_time = models.CharField(max_length=255, blank=True, null=True)
    offduty_check_time_result = models.CharField(max_length=255, blank=True, null=True)
    offduty_check_addr = models.CharField(max_length=255, blank=True, null=True)
    offduty_check_addr_result = models.CharField(max_length=255, blank=True, null=True)
    is_workday = models.IntegerField(blank=True, null=True)
    check_event_id = models.CharField(max_length=40, blank=True, null=True)
    sync_status = models.CharField(max_length=255, blank=True, null=True)
    onduty_user_longitude = models.FloatField(blank=True, null=True)
    onduty_user_latitude = models.FloatField(blank=True, null=True)
    offduty_user_longitude = models.FloatField(blank=True, null=True)
    offduty_user_latitude = models.FloatField(blank=True, null=True)
    approve_id = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    hrm_comments_id = models.CharField(max_length=50, blank=True, null=True)
    hrm_adjust_id = models.CharField(max_length=40, blank=True, null=True)
    is_question = models.IntegerField(blank=True, null=True)
    days = models.FloatField(blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    attendance_type = models.CharField(max_length=50, blank=True, null=True)
    second_attendance_type = models.CharField(max_length=50, blank=True, null=True)
    is_suspected = models.CharField(max_length=2, blank=True, null=True)
    rest_days = models.FloatField(blank=True, null=True)
    second_rest_days = models.FloatField(blank=True, null=True)
    wf_no = models.CharField(max_length=50, blank=True, null=True)
    second_wf_no = models.CharField(max_length=50, blank=True, null=True)
    late_time = models.FloatField(blank=True, null=True)
    early_time = models.FloatField(blank=True, null=True)
    onduty_address = models.CharField(max_length=255, blank=True, null=True)
    offduty_address = models.CharField(max_length=255, blank=True, null=True)
    onduty_city_id = models.CharField(max_length=255, blank=True, null=True)
    offduty_city_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_baseinfo'


class AttendanceHrmAdjust(models.Model):
    hrm_adjust_id = models.CharField(primary_key=True, max_length=40)
    attendance_baseinfo_id = models.CharField(max_length=50, blank=True, null=True)
    op_user_id = models.CharField(max_length=80, blank=True, null=True)
    comments = models.CharField(max_length=300, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    projectid = models.CharField(max_length=50, blank=True, null=True)
    attendance_type = models.CharField(max_length=50, blank=True, null=True)
    days = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    projectid_new = models.CharField(max_length=50, blank=True, null=True)
    attendance_new = models.CharField(max_length=50, blank=True, null=True)
    days_new = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    rest_days = models.FloatField(blank=True, null=True)
    address = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_hrm_adjust'


class AttendanceTypeConf(models.Model):
    attendance_type_conf_id = models.CharField(primary_key=True, max_length=50)
    attendance_type = models.CharField(max_length=50)
    is_calc_work_day = models.IntegerField(blank=True, null=True)
    attendance_type_name = models.CharField(max_length=50)
    attendance_code = models.CharField(max_length=10, blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_type_conf'


class AttendanceWhiteList(models.Model):
    white_id = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    start_ym = models.CharField(max_length=255, blank=True, null=True)
    end_ym = models.CharField(max_length=255, blank=True, null=True)
    op_user = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'attendance_white_list'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group_id = models.IntegerField()
    permission_id = models.IntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group_id', 'permission_id'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type_id = models.IntegerField()
    codename = models.CharField(max_length=100)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type_id', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    email = models.CharField(unique=True, max_length=255)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    user_type_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'auth_user'


class BillManage(models.Model):
    bill_id = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    bill_code = models.CharField(max_length=225, blank=True, null=True)
    create_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'bill_manage'


class ChbreportGitcommitinfo(models.Model):
    p_id = models.CharField(primary_key=True, max_length=50)
    ref = models.CharField(max_length=500, blank=True, null=True)
    project_id = models.CharField(max_length=500, blank=True, null=True)
    project_name = models.CharField(max_length=500, blank=True, null=True)
    commit_id = models.CharField(max_length=500, blank=True, null=True)
    commit_message = models.CharField(max_length=500, blank=True, null=True)
    commit_time = models.DateTimeField(blank=True, null=True)
    commit_additions = models.IntegerField(blank=True, null=True)
    commit_deletions = models.IntegerField(blank=True, null=True)
    commit_total = models.IntegerField(blank=True, null=True)
    commit_author_name = models.CharField(max_length=500, blank=True, null=True)
    commit_author_email = models.CharField(max_length=500, blank=True, null=True)
    batch_id = models.CharField(max_length=500, blank=True, null=True)
    path_with_namespace = models.CharField(max_length=500, blank=True, null=True)
    commit_name = models.CharField(max_length=500, blank=True, null=True)
    cms_user_id = models.CharField(max_length=500, blank=True, null=True)
    cms_user_name = models.CharField(max_length=500, blank=True, null=True)
    cms_user_nick = models.CharField(max_length=500, blank=True, null=True)
    issue_key = models.CharField(max_length=50, blank=True, null=True)
    group_id = models.CharField(max_length=100, blank=True, null=True)
    artifact_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chbreport_gitcommitinfo'


class ChbreportGituserFix(models.Model):
    p_id = models.CharField(primary_key=True, max_length=50)
    cms_user_name = models.CharField(max_length=500, blank=True, null=True)
    git_user_name = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'chbreport_gituser_fix'


class ComputerAided(models.Model):
    computer_aided_id = models.CharField(primary_key=True, max_length=50)
    userno = models.CharField(max_length=50)
    bym = models.IntegerField(blank=True, null=True)
    eym = models.IntegerField(blank=True, null=True)
    aided_permonth = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'computer_aided'


class Contract(models.Model):
    contract_id = models.CharField(primary_key=True, max_length=50)
    customert_id = models.CharField(max_length=50, blank=True, null=True)
    hrm_department_id = models.CharField(max_length=5, blank=True, null=True)
    contract_type = models.CharField(max_length=2, blank=True, null=True)
    contract_code = models.CharField(max_length=50, blank=True, null=True)
    contract_name = models.CharField(max_length=100, blank=True, null=True)
    product = models.CharField(max_length=1000, blank=True, null=True)
    amount_notinclude_tax = models.FloatField(blank=True, null=True)
    amount = models.FloatField(blank=True, null=True)
    sing_time = models.DateField(blank=True, null=True)
    party_a = models.CharField(max_length=50, blank=True, null=True)
    party_b = models.CharField(max_length=50, blank=True, null=True)
    beg_time = models.DateField(blank=True, null=True)
    end_time = models.DateField(blank=True, null=True)
    coll_pay_type = models.CharField(max_length=50, blank=True, null=True)
    is_main = models.CharField(max_length=50, blank=True, null=True)
    main_contract_id = models.CharField(max_length=50, blank=True, null=True)
    tax_rate = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    cost_rate = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    add_time = models.DateField(blank=True, null=True)
    op_user = models.CharField(max_length=50, blank=True, null=True)
    contract_statu = models.CharField(max_length=2, blank=True, null=True)
    convention = models.CharField(max_length=500, blank=True, null=True)
    pay_terms = models.CharField(max_length=500, blank=True, null=True)
    guarantee_period = models.IntegerField(blank=True, null=True)
    sale_area = models.CharField(max_length=50, blank=True, null=True)
    corp_code = models.CharField(max_length=4, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    party_a_charge = models.CharField(max_length=50, blank=True, null=True)
    party_b_charge = models.CharField(max_length=50, blank=True, null=True)
    sub_contract_father_id = models.CharField(max_length=50, blank=True, null=True)
    sale_type = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract'


class ContractCollectPay(models.Model):
    contract_collect_pay_id = models.CharField(primary_key=True, max_length=50)
    contract_id = models.CharField(max_length=50, blank=True, null=True)
    project_costs_id = models.CharField(max_length=50, blank=True, null=True)
    op_user = models.CharField(max_length=50, blank=True, null=True)
    collect_pay_user = models.CharField(max_length=50, blank=True, null=True)
    collect_pay_quota = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    collect_pay_type = models.CharField(max_length=2, blank=True, null=True)
    comments = models.CharField(max_length=500, blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    quota_take_time = models.DateField(blank=True, null=True)
    voucher_number = models.CharField(max_length=50, blank=True, null=True)
    project_code = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract_collect_pay'


class ContractInvoicing(models.Model):
    contract_invoicing_id = models.CharField(primary_key=True, max_length=50)
    contract_id = models.CharField(max_length=50, blank=True, null=True)
    invoicing_corp_name = models.CharField(max_length=500, blank=True, null=True)
    voucher_number = models.CharField(max_length=50, blank=True, null=True)
    invoicing_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    invoicing_type = models.CharField(max_length=2, blank=True, null=True)
    invoicing_date = models.DateField(blank=True, null=True)
    tax_rate = models.CharField(max_length=50, blank=True, null=True)
    invoicing_in_out = models.CharField(max_length=2, blank=True, null=True)
    project_code = models.CharField(max_length=50, blank=True, null=True)
    op_user = models.CharField(max_length=50, blank=True, null=True)
    comments = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract_invoicing'


class ContractProjectCostRel(models.Model):
    contract_project_cost_rel_id = models.CharField(primary_key=True, max_length=50)
    contract_id = models.CharField(max_length=50, blank=True, null=True)
    project_costs_id = models.CharField(max_length=50, blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    rel_type = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'contract_project_cost_rel'


class ContractProjectRel(models.Model):
    contract_project_rel_id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50)
    contract_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'contract_project_rel'


class CorpBankAmountFlow(models.Model):
    bank_amount_flow_id = models.CharField(primary_key=True, max_length=50)
    bank_id = models.CharField(max_length=50, blank=True, null=True)
    amount = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    flow_type = models.CharField(max_length=50, blank=True, null=True)
    transaction_time = models.DateTimeField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    add_user = models.CharField(max_length=50, blank=True, null=True)
    amount_type = models.CharField(max_length=2, blank=True, null=True)
    comment = models.CharField(max_length=255, blank=True, null=True)
    closing_balance = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    opening_balance = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    bank_amount_flow_no = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corp_bank_amount_flow'


class CorpBankInfo(models.Model):
    bank_id = models.CharField(primary_key=True, max_length=50)
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    bank_no = models.CharField(max_length=50, blank=True, null=True)
    corp_ip = models.CharField(max_length=50, blank=True, null=True)
    parent_corp_id = models.CharField(max_length=50, blank=True, null=True)
    beg_balance = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    beg_balance_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corp_bank_info'


class CorpLaborMonth(models.Model):
    corp_labor_month_id = models.CharField(primary_key=True, max_length=50)
    cost_type = models.CharField(max_length=50, blank=True, null=True)
    cost = models.DecimalField(max_digits=9, decimal_places=2, blank=True, null=True)
    ym = models.IntegerField(blank=True, null=True)
    addtime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'corp_labor_month'


class CostTypeName(models.Model):
    wf_cost_type = models.CharField(primary_key=True, max_length=255)
    cost_name = models.CharField(max_length=255, blank=True, null=True)
    project_cost_type = models.CharField(max_length=255, blank=True, null=True)
    order_index = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cost_type_name'


class Customer(models.Model):
    customert_id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=50, blank=True, null=True)
    belong_sale_arae = models.CharField(max_length=2, blank=True, null=True)
    customert_type = models.CharField(max_length=50, blank=True, null=True)
    default_traval_allowance = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    default_project_shortname = models.CharField(max_length=20, blank=True, null=True)
    area_charge = models.CharField(max_length=50, blank=True, null=True)
    sale_charge = models.CharField(max_length=50, blank=True, null=True)
    province = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerManHour(models.Model):
    customer_man_hour_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    customer_man_hour_code = models.CharField(max_length=50, blank=True, null=True)
    customer_man_hour_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_man_hour'


class DevelopingCosts(models.Model):
    developing_costs_id = models.CharField(primary_key=True, max_length=50)
    costs = models.DecimalField(max_digits=12, decimal_places=2)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    create_time = models.DateTimeField()
    project_id = models.CharField(max_length=50, blank=True, null=True)
    hrm_department_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'developing_costs'


class DingtalkAreaCode(models.Model):
    area_code = models.CharField(max_length=50)
    area_code_name = models.CharField(max_length=50)
    comments = models.CharField(max_length=225, blank=True, null=True)
    default_traval_allowance = models.FloatField(blank=True, null=True)
    dingtalk_area_code_id = models.CharField(primary_key=True, max_length=50)
    work_day = models.DecimalField(max_digits=2, decimal_places=1, blank=True, null=True)
    project_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dingtalk_area_code'


class DingtalkAreaMappingInfo(models.Model):
    area_mapping_info_id = models.CharField(primary_key=True, max_length=50)
    area_code = models.CharField(max_length=50)
    match_area_location = models.CharField(max_length=200)
    comments = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dingtalk_area_mapping_info'


class DingtalkAttendance(models.Model):
    work_date = models.DateField(primary_key=True)
    user_id = models.CharField(max_length=80)
    onduty_check_time = models.BigIntegerField(blank=True, null=True)
    onduty_check_time_result = models.CharField(max_length=255, blank=True, null=True)
    onduty_check_addr = models.CharField(max_length=255, blank=True, null=True)
    onduty_check_addr_result = models.CharField(max_length=255, blank=True, null=True)
    offduty_check_time = models.BigIntegerField(blank=True, null=True)
    offduty_check_time_result = models.CharField(max_length=255, blank=True, null=True)
    offduty_check_addr = models.CharField(max_length=255, blank=True, null=True)
    offduty_check_addr_result = models.CharField(max_length=255, blank=True, null=True)
    is_workday = models.IntegerField(blank=True, null=True)
    check_event_id = models.CharField(max_length=40, blank=True, null=True)
    sync_status = models.CharField(max_length=255, blank=True, null=True)
    flag_auto = models.CharField(max_length=30, blank=True, null=True)
    flag_name_auto = models.CharField(max_length=50, blank=True, null=True)
    flag_hrm = models.CharField(max_length=30, blank=True, null=True)
    flag_name_hrm = models.CharField(max_length=50, blank=True, null=True)
    onduty_user_longitude = models.FloatField(blank=True, null=True)
    onduty_user_latitude = models.FloatField(blank=True, null=True)
    offduty_user_longitude = models.FloatField(blank=True, null=True)
    offduty_user_latitude = models.FloatField(blank=True, null=True)
    approve_id = models.CharField(max_length=50, blank=True, null=True)
    is_on_business = models.IntegerField(blank=True, null=True)
    overtime_hour = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    hrm_comments_id = models.CharField(max_length=50, blank=True, null=True)
    hrm_adjust_id = models.CharField(max_length=40, blank=True, null=True)
    is_question = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dingtalk_attendance'
        unique_together = (('work_date', 'user_id'),)


class DingtalkAttendanceComment(models.Model):
    dingtalk_attendance_comment_id = models.CharField(primary_key=True, max_length=50)
    op_user_id = models.CharField(max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dingtalk_attendance_comment'


class DingtalkAttendanceDetail(models.Model):
    dingtalk_attendance_id = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(max_length=80, blank=True, null=True)
    work_date = models.BigIntegerField(blank=True, null=True)
    digtalk_attendance_event_id = models.CharField(max_length=50, blank=True, null=True)
    check_type = models.CharField(max_length=10, blank=True, null=True)
    time_result = models.CharField(max_length=50, blank=True, null=True)
    location_result = models.CharField(max_length=50, blank=True, null=True)
    base_check_time = models.BigIntegerField(blank=True, null=True)
    user_check_time = models.BigIntegerField(blank=True, null=True)
    outside_remark = models.CharField(max_length=200, blank=True, null=True)
    base_address = models.CharField(max_length=200, blank=True, null=True)
    user_address = models.CharField(max_length=200, blank=True, null=True)
    base_longitude = models.FloatField(blank=True, null=True)
    user_longitude = models.FloatField(blank=True, null=True)
    base_latitude = models.FloatField(blank=True, null=True)
    user_latitude = models.FloatField(blank=True, null=True)
    procinst_id = models.CharField(max_length=50, blank=True, null=True)
    approve_id = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    op_user_id = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'dingtalk_attendance_detail'


class DingtalkAttendanceEvent(models.Model):
    dingtalk_attendance_event_id = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(max_length=80, blank=True, null=True)
    work_month = models.CharField(max_length=10, blank=True, null=True)
    op_user_id = models.CharField(max_length=50, blank=True, null=True)
    dingtalk_attendance_event_status = models.CharField(max_length=10, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField()
    attendance_new = models.CharField(max_length=50)
    days = models.DecimalField(max_digits=2, decimal_places=0)
    status = models.CharField(max_length=50, blank=True, null=True)
    pictures = models.CharField(max_length=10000, blank=True, null=True)
    include_holiday = models.CharField(max_length=50, blank=True, null=True)
    projectid_new = models.CharField(max_length=50, blank=True, null=True)
    op_comments = models.CharField(max_length=1000, blank=True, null=True)
    province_city = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dingtalk_attendance_event'


class DingtalkAttendanceHrmAdjust(models.Model):
    hrm_adjust_id = models.CharField(primary_key=True, max_length=40)
    before_flag_auto = models.CharField(max_length=30, blank=True, null=True)
    before_flag_name_auto = models.CharField(max_length=30, blank=True, null=True)
    before_flag_hrm = models.CharField(max_length=30, blank=True, null=True)
    before_flag_name_hrm = models.CharField(max_length=30, blank=True, null=True)
    flag_hrm = models.CharField(max_length=30, blank=True, null=True)
    flag_name_hrm = models.CharField(max_length=30, blank=True, null=True)
    work_date = models.DateField(blank=True, null=True)
    user_id = models.CharField(max_length=80, blank=True, null=True)
    op_user_id = models.CharField(max_length=80, blank=True, null=True)
    comments = models.CharField(max_length=300, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dingtalk_attendance_hrm_adjust'


class DingtalkCheckin(models.Model):
    userid = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=30, blank=True, null=True)
    checkin_time = models.DateTimeField()
    image_list = models.CharField(max_length=500, blank=True, null=True)
    detail_place = models.CharField(max_length=200, blank=True, null=True)
    remark = models.CharField(max_length=200, blank=True, null=True)
    place = models.CharField(max_length=100, blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dingtalk_checkin'
        unique_together = (('userid', 'checkin_time'),)


class DingtalkDepartment(models.Model):
    dingtalk_department_id = models.CharField(primary_key=True, max_length=50)
    department_name = models.CharField(max_length=200, blank=True, null=True)
    department_pid = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    department_arch = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dingtalk_department'


class DingtalkDepartmentCopy(models.Model):
    dingtalk_department_id = models.CharField(primary_key=True, max_length=50)
    department_name = models.CharField(max_length=200, blank=True, null=True)
    department_pid = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    department_arch = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dingtalk_department_copy'


class DingtalkMappingProject(models.Model):
    mapping_id = models.CharField(primary_key=True, max_length=50)
    dingding_addres = models.CharField(max_length=500, blank=True, null=True)
    project_code = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dingtalk_mapping_project'


class DingtalkProcessInstance(models.Model):
    procinst_id = models.CharField(primary_key=True, max_length=50)
    dingtalk_user_id = models.CharField(max_length=50, blank=True, null=True)
    dingtalk_department_id = models.CharField(max_length=50, blank=True, null=True)
    approve_type = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    process_status = models.CharField(max_length=15, blank=True, null=True)
    process_instance_result = models.CharField(max_length=15, blank=True, null=True)
    origin_leave_start = models.CharField(max_length=30, blank=True, null=True)
    origin_leave_end = models.CharField(max_length=30, blank=True, null=True)
    origin_leave_time = models.FloatField(blank=True, null=True)
    time_type = models.CharField(max_length=10, blank=True, null=True)
    leave_start = models.DateTimeField(blank=True, null=True)
    leave_end = models.DateTimeField(blank=True, null=True)
    leave_time = models.FloatField(blank=True, null=True)
    leave_reason = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dingtalk_process_instance'


class DingtalkUser(models.Model):
    dingtalk_user_id = models.CharField(primary_key=True, max_length=50)
    dingtalk_name = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    jobnumber = models.CharField(max_length=64, blank=True, null=True)
    hireddate = models.DateTimeField(blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    base_check_addr = models.CharField(max_length=3, blank=True, null=True)
    comments = models.CharField(max_length=225, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    dingtalk_department_structure = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dingtalk_user'


class DingtalkUserCopy(models.Model):
    dingtalk_user_id = models.CharField(primary_key=True, max_length=50)
    dingtalk_name = models.CharField(max_length=20, blank=True, null=True)
    mobile = models.CharField(max_length=11, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    jobnumber = models.CharField(max_length=64, blank=True, null=True)
    hireddate = models.DateTimeField(blank=True, null=True)
    department = models.CharField(max_length=100, blank=True, null=True)
    base_check_addr = models.CharField(max_length=3, blank=True, null=True)
    comments = models.CharField(max_length=225, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    dingtalk_department_structure = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dingtalk_user_copy'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type_id = models.IntegerField(blank=True, null=True)
    user_id = models.IntegerField()

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


class DjiangoCache(models.Model):
    cache_key = models.CharField(primary_key=True, max_length=255)
    value = models.TextField()
    expires = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'djiango_cache'


class EventLog(models.Model):
    event_log_id = models.AutoField(primary_key=True)
    event_type = models.CharField(max_length=50)
    event_code = models.CharField(max_length=50)
    bus_id = models.CharField(unique=True, max_length=50, blank=True, null=True)
    property_1 = models.CharField(max_length=200, blank=True, null=True)
    op_user_id = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'event_log'


class HolidaysAndFestivals(models.Model):
    date = models.DateField(primary_key=True)
    type = models.CharField(max_length=50, blank=True, null=True)
    festival_name = models.CharField(max_length=50, blank=True, null=True)
    legal = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'holidays_and_festivals'


class HrmAttendance(models.Model):
    hrm_attendance_id = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    attendance_date = models.DateField(blank=True, null=True)
    attendance_start_time = models.DateTimeField(blank=True, null=True)
    attendance_end_time = models.DateTimeField(blank=True, null=True)
    hrm_attendance_event_id = models.CharField(max_length=50, blank=True, null=True)
    comments = models.CharField(max_length=225, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'hrm_attendance'


class HrmAttendanceEvent(models.Model):
    hrm_attendance_event_id = models.CharField(primary_key=True, max_length=50)
    op_user_id = models.CharField(max_length=50, blank=True, null=True)
    hrm_attendance_event_status = models.CharField(max_length=10, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hrm_attendance_event'


class HrmDepartment(models.Model):
    hrm_department_id = models.CharField(primary_key=True, max_length=50)
    hrm_department_name = models.CharField(max_length=200, blank=True, null=True)
    hrm_department_pid = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    hrm_department_level = models.CharField(max_length=5, blank=True, null=True)
    hrm_department_id_level3 = models.CharField(max_length=5, blank=True, null=True)
    hrm_department_arch = models.CharField(max_length=300, blank=True, null=True)
    dingtalk_department_id = models.CharField(max_length=50, blank=True, null=True)
    is_del = models.CharField(max_length=5, blank=True, null=True)
    department_manager = models.CharField(max_length=50, blank=True, null=True)
    order_index = models.CharField(max_length=2, blank=True, null=True)
    dep_head_id = models.CharField(max_length=50, blank=True, null=True)
    dep_sup_head_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hrm_department'


class HrmDepartmentBak(models.Model):
    hrm_department_id = models.CharField(primary_key=True, max_length=5)
    hrm_department_name = models.CharField(max_length=200, blank=True, null=True)
    hrm_department_pid = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    hrm_department_level = models.CharField(max_length=5, blank=True, null=True)
    hrm_department_id_level3 = models.CharField(max_length=5, blank=True, null=True)
    hrm_department_arch = models.CharField(max_length=300, blank=True, null=True)
    dingtalk_department_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hrm_department_bak'


class HrmJobActivities(models.Model):
    hrm_job_activities_id = models.CharField(primary_key=True, max_length=50)
    hrm_job_activities_name = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    stage = models.CharField(max_length=5, blank=True, null=True)
    hrm_job_group_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hrm_job_activities'


class HrmJobGroup(models.Model):
    hrm_job_group_id = models.CharField(primary_key=True, max_length=50)
    hrm_job_group_name = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hrm_job_group'


class HrmJobtitle(models.Model):
    hrm_jobtitle_id = models.CharField(primary_key=True, max_length=50)
    hrm_jobtitle_name = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    hrm_department_id = models.CharField(max_length=50, blank=True, null=True)
    hrm_job_activities_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hrm_jobtitle'


class HrmLocations(models.Model):
    hrm_locations_id = models.CharField(primary_key=True, max_length=3)
    hrm_locations_name = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    dingtalk_base_addr = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hrm_locations'


class HrmResources(models.Model):
    id = models.CharField(max_length=255, blank=True, null=True)
    director = models.CharField(max_length=255, blank=True, null=True)
    jobtitle_level = models.CharField(max_length=255, blank=True, null=True)
    birthday = models.CharField(max_length=255, blank=True, null=True)
    job_title = models.CharField(max_length=255, blank=True, null=True)
    work_code = models.CharField(max_length=255, blank=True, null=True)
    lastname = models.CharField(max_length=255, blank=True, null=True)
    social_service = models.CharField(max_length=255, blank=True, null=True)
    it_working_time = models.CharField(max_length=255, blank=True, null=True)
    graduation_time = models.CharField(max_length=255, blank=True, null=True)
    record_schooling = models.CharField(max_length=255, blank=True, null=True)
    graduate_school = models.CharField(max_length=255, blank=True, null=True)
    id_card = models.CharField(max_length=255, blank=True, null=True)
    in_the_time = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hrm_resources'


class Hupan(models.Model):
    project_costs_id = models.CharField(max_length=50)
    project_costs_gen_eid = models.CharField(max_length=50, blank=True, null=True)
    ym = models.IntegerField()
    cost_effect_time = models.DateField(blank=True, null=True)
    project_code = models.CharField(max_length=50, blank=True, null=True)
    costs = models.DecimalField(max_digits=9, decimal_places=2)
    depid = models.CharField(max_length=50, blank=True, null=True)
    cost_type = models.CharField(max_length=2)
    userno = models.CharField(max_length=50, blank=True, null=True)
    data_src = models.CharField(max_length=2)
    addtime = models.DateTimeField(blank=True, null=True)
    adduser = models.CharField(max_length=50, blank=True, null=True)
    project_cost_allocation_id = models.CharField(max_length=50, blank=True, null=True)
    allocation_from_project = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'hupan'


class IpAddress(models.Model):
    ip_address_id = models.AutoField(primary_key=True)
    ip = models.CharField(max_length=500, blank=True, null=True)
    ip_mask = models.CharField(max_length=500, blank=True, null=True)
    ip_address = models.CharField(max_length=500, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=500, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ip_address'


class ManHourAuditUserEventLog(models.Model):
    man_hour_audit_user_event_log_id = models.CharField(primary_key=True, max_length=50)
    proejct_man_hour_audit_user_id = models.CharField(max_length=50)
    create_time = models.DateTimeField()
    op_user = models.CharField(max_length=225)
    op_type = models.CharField(max_length=255)
    project_stage_id = models.CharField(max_length=11, blank=True, null=True)
    work_domain_code = models.CharField(max_length=200, blank=True, null=True)
    first_approver = models.CharField(max_length=50, blank=True, null=True)
    second_approver = models.CharField(max_length=50, blank=True, null=True)
    project_stage_id_new = models.CharField(max_length=11, blank=True, null=True)
    work_domain_code_new = models.CharField(max_length=200, blank=True, null=True)
    first_approver_new = models.CharField(max_length=50, blank=True, null=True)
    second_approver_new = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'man_hour_audit_user_event_log'


class ManhourAutoCreateConf(models.Model):
    auto_create_id = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    project_code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'manhour_auto_create_conf'


class ManhourMyproject(models.Model):
    manhour_myproject = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(max_length=100)
    project_primary_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'manhour_myproject'


class MealAllowanceArchive(models.Model):
    meal_allowance_archive_id = models.CharField(primary_key=True, max_length=50)
    ym = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    userno = models.CharField(max_length=50)
    zc = models.IntegerField(blank=True, null=True)
    wc = models.IntegerField(blank=True, null=True)
    op_user = models.CharField(max_length=50, blank=True, null=True)
    op_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meal_allowance_archive'


class MonitorActiveTest(models.Model):
    active_test_id = models.CharField(primary_key=True, max_length=50)
    host_id = models.CharField(max_length=500, blank=True, null=True)
    host_name = models.CharField(max_length=500, blank=True, null=True)
    active_test_name = models.CharField(max_length=500, blank=True, null=True)
    test_ip = models.CharField(max_length=500, blank=True, null=True)
    test_port = models.CharField(max_length=500, blank=True, null=True)
    test_url = models.CharField(max_length=1000, blank=True, null=True)
    test_sql = models.CharField(max_length=1000, blank=True, null=True)
    test_type = models.CharField(max_length=255)
    add_time = models.DateTimeField()
    applications = models.CharField(max_length=255, blank=True, null=True)
    delay = models.CharField(max_length=500, blank=True, null=True)
    value_type = models.CharField(max_length=50, blank=True, null=True)
    trigger_id = models.CharField(max_length=50, blank=True, null=True)
    request_method = models.CharField(max_length=50, blank=True, null=True)
    trigger_name = models.CharField(max_length=500, blank=True, null=True)
    key_field = models.CharField(db_column='key_', max_length=500, blank=True, null=True)  # Field renamed because it ended with '_'.
    output_format = models.CharField(max_length=50, blank=True, null=True)
    item_id = models.CharField(max_length=50, blank=True, null=True)
    test_install_soft_id = models.CharField(max_length=50, blank=True, null=True)
    test_proxy_param = models.CharField(max_length=255, blank=True, null=True)
    soft_user_type = models.CharField(max_length=255, blank=True, null=True)
    test_sql_code = models.CharField(max_length=255, blank=True, null=True)
    test_sql_dbuser = models.CharField(max_length=100, blank=True, null=True)
    test_sql_dbpwd = models.CharField(max_length=100, blank=True, null=True)
    soft_user_id = models.CharField(max_length=100, blank=True, null=True)
    project_code = models.CharField(max_length=100, blank=True, null=True)
    active_test_target = models.CharField(max_length=100, blank=True, null=True)
    alertitem_code = models.CharField(max_length=50, blank=True, null=True)
    expression = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'monitor_active_test'


class OaFwPushData(models.Model):
    oa_fw_push_data_id = models.CharField(primary_key=True, max_length=50)
    wf_no = models.CharField(max_length=50, blank=True, null=True)
    wf_name = models.CharField(max_length=255, blank=True, null=True)
    wf_add_time = models.DateTimeField(blank=True, null=True)
    wf_final_approve_time = models.DateTimeField(blank=True, null=True)
    wf_add_user = models.CharField(max_length=50, blank=True, null=True)
    wf_belong_dep = models.CharField(max_length=255, blank=True, null=True)
    wf_project_id = models.CharField(max_length=50, blank=True, null=True)
    wf_cost_type = models.CharField(max_length=50, blank=True, null=True)
    wf_cost_sum = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wf_contract_no = models.CharField(max_length=255, blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    gen_busi_statu = models.CharField(max_length=50, blank=True, null=True)
    gen_busi_id = models.CharField(max_length=50, blank=True, null=True)
    gen_cost_id = models.CharField(max_length=50, blank=True, null=True)
    gen_cost_statu = models.CharField(max_length=50, blank=True, null=True)
    data_text = models.TextField(blank=True, null=True)
    wf_payee = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'oa_fw_push_data'


class PaymentDetail(models.Model):
    payment_detail_id = models.CharField(primary_key=True, max_length=50)
    sno = models.CharField(max_length=255, blank=True, null=True)
    bank_no = models.CharField(max_length=100, blank=True, null=True)
    cost_total = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    cost_time = models.CharField(max_length=50, blank=True, null=True)
    payee = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    op_user = models.CharField(max_length=255, blank=True, null=True)
    payment_flow_id = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_detail'


class PaymentFlow(models.Model):
    payment_flow_id = models.CharField(primary_key=True, max_length=50)
    wf_no = models.CharField(unique=True, max_length=255, blank=True, null=True)
    wf_cost_sum = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    wf_payee = models.CharField(max_length=255, blank=True, null=True)
    wf_bank_card = models.CharField(max_length=255, blank=True, null=True)
    is_sure = models.CharField(max_length=2, blank=True, null=True)
    payment_detail_id = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'payment_flow'


class Personsalary(models.Model):
    personsalary_id = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    user_name = models.CharField(max_length=50, blank=True, null=True)
    sal_type = models.CharField(max_length=20, blank=True, null=True)
    sal_val = models.CharField(max_length=200, blank=True, null=True)
    ym = models.IntegerField(blank=True, null=True)
    project = models.CharField(max_length=50, blank=True, null=True)
    comment = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personsalary'
        unique_together = (('user_id', 'ym', 'sal_type'),)


class PersonsalaryDetail(models.Model):
    personsalary_detail_id = models.CharField(primary_key=True, max_length=50)
    personsalary_id = models.CharField(max_length=50, blank=True, null=True)
    sal_val = models.FloatField(blank=True, null=True)
    project_code = models.CharField(max_length=50, blank=True, null=True)
    area_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personsalary_detail'


class PlanTask(models.Model):
    plan_task_id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=255, blank=True, null=True)
    user_id = models.CharField(max_length=255, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    per = models.FloatField(blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    op_user = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'plan_task'


class Project(models.Model):
    project_primary_id = models.AutoField(primary_key=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    project_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    pid = models.CharField(max_length=50, blank=True, null=True)
    project_manager = models.CharField(max_length=50, blank=True, null=True)
    man_hour_audit_user = models.CharField(max_length=50, blank=True, null=True)
    project_event_id = models.CharField(max_length=50, blank=True, null=True)
    project_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    project_name_old = models.CharField(max_length=50, blank=True, null=True)
    project_proposer = models.CharField(max_length=50, blank=True, null=True)
    project_start_time = models.CharField(max_length=555, blank=True, null=True)
    project_end_time = models.CharField(max_length=555, blank=True, null=True)
    project_demand = models.TextField(blank=True, null=True)
    project_target = models.TextField(blank=True, null=True)
    project_risk = models.TextField(blank=True, null=True)
    project_risk_solution = models.TextField(blank=True, null=True)
    project_member_id = models.CharField(max_length=50, blank=True, null=True)
    project_budget = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    project_type = models.CharField(max_length=10, blank=True, null=True)
    project_kind = models.CharField(max_length=50, blank=True, null=True)
    second_party_contacts = models.CharField(max_length=50, blank=True, null=True)
    project_region = models.CharField(max_length=50, blank=True, null=True)
    first_party_contacts = models.CharField(max_length=50, blank=True, null=True)
    first_party_contacts_phone = models.CharField(max_length=50, blank=True, null=True)
    first_party_unit_name = models.CharField(max_length=200, blank=True, null=True)
    first_party_unit_summary = models.CharField(max_length=1000, blank=True, null=True)
    sales_manager = models.CharField(max_length=50, blank=True, null=True)
    development_manager = models.CharField(max_length=50, blank=True, null=True)
    test_manage = models.CharField(max_length=50, blank=True, null=True)
    project_alias = models.CharField(max_length=200, blank=True, null=True)
    req_time = models.DateTimeField(blank=True, null=True)
    consensusor = models.CharField(max_length=50, blank=True, null=True)
    hospital_scale = models.CharField(max_length=5000, blank=True, null=True)
    project_approve_event_id = models.CharField(max_length=50, blank=True, null=True)
    project_progress = models.TextField(blank=True, null=True)
    confluence_workspace = models.CharField(max_length=1000, blank=True, null=True)
    jira_workspace = models.CharField(max_length=1000, blank=True, null=True)
    svn_workspace = models.CharField(max_length=1000, blank=True, null=True)
    attachment_path = models.CharField(max_length=1000, blank=True, null=True)
    contact_date = models.CharField(max_length=555, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    project_req_date = models.CharField(max_length=2000, blank=True, null=True)
    product_target = models.TextField(blank=True, null=True)
    project_core_method = models.TextField(blank=True, null=True)
    apply_department = models.CharField(max_length=50, blank=True, null=True)
    apply_position = models.CharField(max_length=50, blank=True, null=True)
    project_status = models.CharField(max_length=50, blank=True, null=True)
    project_sub_class = models.CharField(max_length=50, blank=True, null=True)
    is_complete = models.CharField(max_length=50, blank=True, null=True)
    project_complete_time = models.DateTimeField(blank=True, null=True)
    workhour_show = models.CharField(max_length=50, blank=True, null=True)
    short_name = models.CharField(max_length=50, blank=True, null=True)
    project_explain = models.CharField(max_length=1000, blank=True, null=True)
    report_show = models.CharField(max_length=50, blank=True, null=True)
    customert_id = models.CharField(max_length=50, blank=True, null=True)
    project_busi_code = models.CharField(max_length=50, blank=True, null=True)
    project_worktime = models.CharField(max_length=50, blank=True, null=True)
    default_traval_allowance = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project'


class ProjectApproveEvent(models.Model):
    project_approve_event_id = models.CharField(max_length=50)
    project_primary_id = models.CharField(max_length=50, blank=True, null=True)
    project_approve_stage_code = models.CharField(max_length=50, blank=True, null=True)
    project_type = models.CharField(max_length=50, blank=True, null=True)
    op_user = models.CharField(max_length=50, blank=True, null=True)
    next_op_role = models.CharField(max_length=50, blank=True, null=True)
    next_op_user = models.CharField(max_length=20, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    order_weight = models.BigAutoField(primary_key=True)

    class Meta:
        managed = False
        db_table = 'project_approve_event'


class ProjectApproveEventConfig(models.Model):
    project_approve_stage_code = models.CharField(max_length=50)
    project_approve_stage_code_text = models.CharField(max_length=50, blank=True, null=True)
    project_type = models.CharField(max_length=50)
    role_id = models.CharField(max_length=50, blank=True, null=True)
    goto = models.CharField(max_length=50, blank=True, null=True)
    go_back = models.CharField(max_length=50, blank=True, null=True)
    page_enable_edit = models.IntegerField()
    can_cancle = models.IntegerField()
    stage_location = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_approve_event_config'
        unique_together = (('project_approve_stage_code', 'project_type'),)


class ProjectBusiCode(models.Model):
    project_busi_code_id = models.CharField(primary_key=True, max_length=50)
    project_busi_code = models.CharField(max_length=50, blank=True, null=True)
    project_busi_name = models.CharField(max_length=50, blank=True, null=True)
    dep_name = models.CharField(max_length=50, blank=True, null=True)
    project_busi_type = models.CharField(max_length=2, blank=True, null=True)
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_busi_code'


class ProjectCopy(models.Model):
    project_primary_id = models.AutoField(primary_key=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    project_code = models.CharField(unique=True, max_length=50, blank=True, null=True)
    pid = models.CharField(max_length=50, blank=True, null=True)
    project_manager = models.CharField(max_length=50, blank=True, null=True)
    man_hour_audit_user = models.CharField(max_length=50, blank=True, null=True)
    project_event_id = models.CharField(max_length=50, blank=True, null=True)
    project_name = models.CharField(unique=True, max_length=50, blank=True, null=True)
    project_name_old = models.CharField(max_length=50, blank=True, null=True)
    project_proposer = models.CharField(max_length=50, blank=True, null=True)
    project_start_time = models.CharField(max_length=555, blank=True, null=True)
    project_end_time = models.CharField(max_length=555, blank=True, null=True)
    project_demand = models.TextField(blank=True, null=True)
    project_target = models.TextField(blank=True, null=True)
    project_risk = models.TextField(blank=True, null=True)
    project_risk_solution = models.TextField(blank=True, null=True)
    project_member_id = models.CharField(max_length=50, blank=True, null=True)
    project_budget = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    project_type = models.CharField(max_length=10, blank=True, null=True)
    project_kind = models.CharField(max_length=50, blank=True, null=True)
    second_party_contacts = models.CharField(max_length=50, blank=True, null=True)
    project_region = models.CharField(max_length=50, blank=True, null=True)
    first_party_contacts = models.CharField(max_length=50, blank=True, null=True)
    first_party_contacts_phone = models.CharField(max_length=50, blank=True, null=True)
    first_party_unit_name = models.CharField(max_length=200, blank=True, null=True)
    first_party_unit_summary = models.CharField(max_length=1000, blank=True, null=True)
    sales_manager = models.CharField(max_length=50, blank=True, null=True)
    development_manager = models.CharField(max_length=50, blank=True, null=True)
    test_manage = models.CharField(max_length=50, blank=True, null=True)
    project_alias = models.CharField(max_length=200, blank=True, null=True)
    req_time = models.DateTimeField(blank=True, null=True)
    consensusor = models.CharField(max_length=50, blank=True, null=True)
    hospital_scale = models.CharField(max_length=5000, blank=True, null=True)
    project_approve_event_id = models.CharField(max_length=50, blank=True, null=True)
    project_progress = models.TextField(blank=True, null=True)
    confluence_workspace = models.CharField(max_length=1000, blank=True, null=True)
    jira_workspace = models.CharField(max_length=1000, blank=True, null=True)
    svn_workspace = models.CharField(max_length=1000, blank=True, null=True)
    attachment_path = models.CharField(max_length=1000, blank=True, null=True)
    contact_date = models.CharField(max_length=555, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    project_req_date = models.CharField(max_length=2000, blank=True, null=True)
    product_target = models.TextField(blank=True, null=True)
    project_core_method = models.TextField(blank=True, null=True)
    apply_department = models.CharField(max_length=50, blank=True, null=True)
    apply_position = models.CharField(max_length=50, blank=True, null=True)
    project_status = models.CharField(max_length=50, blank=True, null=True)
    project_sub_class = models.CharField(max_length=50, blank=True, null=True)
    is_complete = models.CharField(max_length=50, blank=True, null=True)
    project_complete_time = models.DateTimeField(blank=True, null=True)
    workhour_show = models.CharField(max_length=50, blank=True, null=True)
    short_name = models.CharField(max_length=50, blank=True, null=True)
    project_explain = models.CharField(max_length=1000, blank=True, null=True)
    report_show = models.CharField(max_length=50, blank=True, null=True)
    customert_id = models.CharField(max_length=50, blank=True, null=True)
    project_busi_code = models.CharField(max_length=50, blank=True, null=True)
    project_worktime = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_copy'


class ProjectCostAllocation(models.Model):
    project_cost_allocation_id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    cost_allocation_type = models.CharField(max_length=2)
    cost_allocation_rule = models.CharField(max_length=50, blank=True, null=True)
    project_cost_allocation_name = models.CharField(max_length=50, blank=True, null=True)
    include_other_allocation = models.CharField(max_length=2, blank=True, null=True)
    calc_order = models.IntegerField(blank=True, null=True)
    forbid = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_cost_allocation'


class ProjectCostAllocationTarget(models.Model):
    cost_allocation_target_id = models.CharField(primary_key=True, max_length=50)
    project_cost_allocation_id = models.CharField(max_length=50, blank=True, null=True)
    cost_allocation_target_objids = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_cost_allocation_target'


class ProjectCosts(models.Model):
    project_costs_id = models.CharField(primary_key=True, max_length=50)
    project_costs_gen_eid = models.CharField(max_length=50, blank=True, null=True)
    ym = models.IntegerField()
    cost_effect_time = models.DateField(blank=True, null=True)
    project_code = models.CharField(max_length=50, blank=True, null=True)
    costs = models.DecimalField(max_digits=14, decimal_places=2)
    depid = models.CharField(max_length=50, blank=True, null=True)
    cost_type = models.CharField(max_length=2)
    userno = models.CharField(max_length=50, blank=True, null=True)
    data_src = models.CharField(max_length=2)
    addtime = models.DateTimeField(blank=True, null=True)
    adduser = models.CharField(max_length=50, blank=True, null=True)
    project_cost_allocation_id = models.CharField(max_length=50, blank=True, null=True)
    allocation_from_project = models.CharField(max_length=50, blank=True, null=True)
    company = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_costs'


class ProjectCostsGenEvent(models.Model):
    project_costs_gen_eid = models.CharField(primary_key=True, max_length=50)
    gen_params = models.CharField(max_length=50, blank=True, null=True)
    op_user = models.CharField(max_length=50, blank=True, null=True)
    addtime = models.DateTimeField(blank=True, null=True)
    rs_info = models.CharField(max_length=2000, blank=True, null=True)
    rs_statu = models.CharField(max_length=50, blank=True, null=True)
    data_src = models.CharField(max_length=2, blank=True, null=True)
    err_info = models.CharField(max_length=8000, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_costs_gen_event'


class ProjectEvent(models.Model):
    project_event_id = models.CharField(primary_key=True, max_length=50)
    project_status = models.CharField(max_length=10, blank=True, null=True)
    audit_user = models.CharField(max_length=10, blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_event'


class ProjectManHour(models.Model):
    project_man_hour_id = models.CharField(max_length=50)
    take_hour = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    work_content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    matter_code = models.CharField(max_length=50, blank=True, null=True)
    work_date = models.DateField()
    project_man_hour_event_id = models.CharField(max_length=100, blank=True, null=True)
    project_milestone_id = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    project_man_hour_child_id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    work_title = models.CharField(max_length=2000, blank=True, null=True)
    project_stage_id = models.CharField(max_length=50, blank=True, null=True)
    project_stage_code = models.CharField(max_length=50, blank=True, null=True)
    req_user_department_id_level3 = models.CharField(max_length=5, blank=True, null=True)
    req_user_jobtitle_id = models.CharField(max_length=5, blank=True, null=True)
    project_stage_id_old = models.CharField(max_length=50, blank=True, null=True)
    hrm_department_id = models.CharField(max_length=50, blank=True, null=True)
    work_domain_code = models.CharField(max_length=50, blank=True, null=True)
    man_hour_status = models.CharField(max_length=2, blank=True, null=True)
    product_module_code = models.CharField(max_length=50, blank=True, null=True)
    customer_man_hour_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_man_hour'
        unique_together = (('matter_code', 'project_man_hour_child_id'),)


class ProjectManHourAuditUsers(models.Model):
    proejct_man_hour_audit_user_id = models.AutoField(primary_key=True)
    project_stage_id = models.IntegerField(blank=True, null=True)
    work_domain_code = models.CharField(max_length=200)
    first_approver = models.CharField(max_length=50, blank=True, null=True)
    second_approver = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_man_hour_audit_users'
        unique_together = (('project_stage_id', 'work_domain_code'),)


class ProjectManHourCopy(models.Model):
    project_man_hour_id = models.CharField(max_length=50)
    take_hour = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    work_content = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    matter_code = models.CharField(max_length=50, blank=True, null=True)
    work_date = models.DateField()
    project_man_hour_event_id = models.CharField(max_length=100, blank=True, null=True)
    project_milestone_id = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    project_man_hour_child_id = models.CharField(primary_key=True, max_length=50)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    work_title = models.CharField(max_length=2000, blank=True, null=True)
    project_stage_id = models.CharField(max_length=50, blank=True, null=True)
    project_stage_code = models.CharField(max_length=50, blank=True, null=True)
    req_user_department_id_level3 = models.CharField(max_length=5, blank=True, null=True)
    req_user_jobtitle_id = models.CharField(max_length=5, blank=True, null=True)
    project_stage_id_old = models.CharField(max_length=50, blank=True, null=True)
    hrm_department_id = models.CharField(max_length=50, blank=True, null=True)
    work_domain_code = models.CharField(max_length=50, blank=True, null=True)
    product_module_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_man_hour_copy'
        unique_together = (('matter_code', 'project_man_hour_child_id'),)


class ProjectManHourEvent(models.Model):
    project_man_hour_event_id = models.CharField(primary_key=True, max_length=50)
    man_hour_status = models.CharField(max_length=50, blank=True, null=True)
    man_hour_status_child = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    recheck_comments = models.CharField(max_length=225, blank=True, null=True)
    modify_time = models.DateTimeField()
    audit_user = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    user_jobtitle = models.CharField(max_length=50, blank=True, null=True)
    user_department = models.CharField(max_length=50, blank=True, null=True)
    audit_user_jobtitle = models.CharField(max_length=50, blank=True, null=True)
    audit_user_department = models.CharField(max_length=50, blank=True, null=True)
    req_user_id = models.CharField(max_length=50, blank=True, null=True)
    project_stage_id = models.CharField(max_length=50, blank=True, null=True)
    event_log_id = models.CharField(max_length=50, blank=True, null=True)
    req_user_department_id_level3 = models.CharField(max_length=5, blank=True, null=True)
    req_user_jobtitle_id = models.CharField(max_length=5, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_man_hour_event'


class ProjectManHourEventLog(models.Model):
    project_man_hour_event_log_id = models.AutoField(primary_key=True)
    project_man_hour_event_id = models.CharField(max_length=50, blank=True, null=True)
    man_hour_status = models.CharField(max_length=50, blank=True, null=True)
    man_hour_status_child = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    recheck_comments = models.CharField(max_length=225, blank=True, null=True)
    modify_time = models.DateTimeField()
    audit_user = models.CharField(max_length=50, blank=True, null=True)
    second_approver = models.CharField(max_length=50, blank=True, null=True)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    user_jobtitle = models.CharField(max_length=50, blank=True, null=True)
    user_department = models.CharField(max_length=50, blank=True, null=True)
    audit_user_jobtitle = models.CharField(max_length=50, blank=True, null=True)
    audit_user_department = models.CharField(max_length=50, blank=True, null=True)
    req_user_id = models.CharField(max_length=50, blank=True, null=True)
    project_stage_id = models.CharField(max_length=50, blank=True, null=True)
    req_user_department_id_level3 = models.CharField(max_length=5, blank=True, null=True)
    req_user_jobtitle_id = models.CharField(max_length=5, blank=True, null=True)
    work_domain_code = models.CharField(max_length=50, blank=True, null=True)
    product_module_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_man_hour_event_log'


class ProjectMatter(models.Model):
    project_matter_id = models.AutoField(primary_key=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    sys_code = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_matter'
        unique_together = (('project_id', 'sys_code'),)


class ProjectMember(models.Model):
    project_member_id = models.CharField(primary_key=True, max_length=50)
    project_primary_id = models.CharField(max_length=50)
    user_id = models.CharField(max_length=50, blank=True, null=True)
    project_role_id = models.CharField(max_length=10, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_member'


class ProjectMilestone(models.Model):
    project_milestone_id = models.AutoField(primary_key=True)
    project_milestone_pid = models.CharField(max_length=50, blank=True, null=True)
    project_primary_id = models.IntegerField(blank=True, null=True)
    project_id = models.CharField(max_length=50)
    milestone_start_time = models.DateField(blank=True, null=True)
    milestone_actually_finish_time = models.DateField(blank=True, null=True)
    milestone_end_time = models.DateField(blank=True, null=True)
    milestone_content = models.CharField(max_length=500)
    comments = models.TextField(blank=True, null=True)
    project_milestone_status = models.CharField(max_length=50, blank=True, null=True)
    overtime_solution = models.CharField(max_length=1000, blank=True, null=True)
    need_more_time = models.IntegerField(blank=True, null=True)
    overtime_reason = models.CharField(max_length=1000, blank=True, null=True)
    overtime = models.IntegerField(blank=True, null=True)
    sign_back_time = models.DateField(blank=True, null=True)
    work_item = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    sort_order = models.IntegerField(blank=True, null=True)
    is_del = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_milestone'


class ProjectModifyHistory(models.Model):
    project_modify_history_id = models.AutoField(primary_key=True)
    project_primary_id = models.CharField(max_length=50, blank=True, null=True)
    field_name = models.CharField(max_length=50, blank=True, null=True)
    op_user = models.CharField(max_length=200, blank=True, null=True)
    old_value = models.TextField(blank=True, null=True)
    new_value = models.TextField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_modify_history'


class ProjectOa(models.Model):
    project_id = models.CharField(primary_key=True, max_length=50)
    pid = models.CharField(max_length=50, blank=True, null=True)
    project_manager = models.CharField(max_length=50, blank=True, null=True)
    man_hour_audit_user = models.CharField(max_length=50, blank=True, null=True)
    project_event_id = models.CharField(max_length=10, blank=True, null=True)
    project_name = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    project_proposer = models.CharField(max_length=50, blank=True, null=True)
    project_start_time = models.DateTimeField(blank=True, null=True)
    project_end_time = models.DateTimeField(blank=True, null=True)
    project_target = models.TextField(blank=True, null=True)
    project_demand = models.TextField(blank=True, null=True)
    project_risk = models.TextField(blank=True, null=True)
    project_member_id = models.CharField(max_length=50, blank=True, null=True)
    project_budget = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    project_type = models.CharField(max_length=10, blank=True, null=True)
    project_kind = models.CharField(max_length=50, blank=True, null=True)
    second_party_contacts = models.CharField(max_length=50, blank=True, null=True)
    project_region = models.CharField(max_length=50, blank=True, null=True)
    first_party_contacts = models.CharField(max_length=50, blank=True, null=True)
    first_party_contacts_phone = models.CharField(max_length=50, blank=True, null=True)
    first_party_unit_name = models.CharField(max_length=200, blank=True, null=True)
    first_party_unit_summary = models.CharField(max_length=1000, blank=True, null=True)
    oa_bill_no = models.CharField(max_length=50, blank=True, null=True)
    sales_manager = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=5, blank=True, null=True)
    project_req_date = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_oa'


class ProjectStage(models.Model):
    project_stage_id = models.AutoField(primary_key=True)
    project_id = models.CharField(max_length=50, blank=True, null=True)
    man_hour_audit_user_id_abandoned = models.CharField(max_length=50, blank=True, null=True)
    project_stage_code = models.CharField(max_length=50, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'project_stage'
        unique_together = (('project_id', 'project_stage_code'),)


class ProvinceCity(models.Model):
    city_id = models.CharField(primary_key=True, max_length=255)
    name = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province_city'


class ProvinceCityAllowance(models.Model):
    province_city_allowance_id = models.CharField(primary_key=True, max_length=50)
    city_id = models.CharField(max_length=50, blank=True, null=True)
    allowance = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'province_city_allowance'


class ReportMenu(models.Model):
    report_menu_id = models.CharField(primary_key=True, max_length=5)
    menu_text = models.CharField(max_length=50, blank=True, null=True)
    menu_pid = models.CharField(max_length=5, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    report_url = models.CharField(max_length=300, blank=True, null=True)
    menu_status = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'report_menu'


class SysCode(models.Model):
    sys_code = models.CharField(max_length=50)
    sys_code_text = models.CharField(max_length=100, blank=True, null=True)
    sys_code_type = models.CharField(max_length=50, blank=True, null=True)
    p_code = models.CharField(max_length=50, blank=True, null=True)
    property1 = models.CharField(max_length=200, blank=True, null=True)
    property2 = models.CharField(max_length=200, blank=True, null=True)
    property3 = models.CharField(max_length=200, blank=True, null=True)
    order_index = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    status = models.CharField(max_length=10, blank=True, null=True)
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    sys_code_id = models.AutoField(primary_key=True)
    sys_code_type_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_code'


class SysCodeCopy(models.Model):
    sys_code = models.CharField(max_length=50)
    sys_code_text = models.CharField(max_length=100, blank=True, null=True)
    sys_code_type = models.CharField(max_length=50, blank=True, null=True)
    p_code = models.CharField(max_length=50, blank=True, null=True)
    property1 = models.CharField(max_length=200, blank=True, null=True)
    property2 = models.CharField(max_length=200, blank=True, null=True)
    property3 = models.CharField(max_length=200, blank=True, null=True)
    order_index = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    status = models.CharField(max_length=10, blank=True, null=True)
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    sys_code_id = models.AutoField(primary_key=True)
    sys_code_type_name = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_code_copy'


class SysFunc(models.Model):
    func_id = models.CharField(primary_key=True, max_length=100)
    func_code = models.CharField(unique=True, max_length=100)
    menu_id = models.CharField(max_length=100)
    menu_code = models.CharField(max_length=100, blank=True, null=True)
    func_text = models.CharField(max_length=100)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_func'


class SysMailSendEvent(models.Model):
    sys_mail_send_event_id = models.CharField(max_length=50)
    mail_subject = models.CharField(max_length=255, blank=True, null=True)
    mail_content = models.TextField(blank=True, null=True)
    mail_recipient = models.CharField(max_length=200, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_mail_send_event'


class SysMenu(models.Model):
    menu_id = models.CharField(primary_key=True, max_length=100)
    menu_pid = models.CharField(max_length=100, blank=True, null=True)
    menu_text = models.CharField(max_length=100)
    role_id = models.CharField(max_length=100, blank=True, null=True)
    menu_url = models.CharField(max_length=100)
    menu_icon = models.CharField(max_length=100, blank=True, null=True)
    statu = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    menu_icon_css = models.CharField(max_length=20, blank=True, null=True)
    menu_dot = models.CharField(max_length=2, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    new_tab = models.CharField(max_length=5, blank=True, null=True)
    expand = models.CharField(max_length=10, blank=True, null=True)
    comments = models.CharField(max_length=225, blank=True, null=True)
    menu_url_type = models.CharField(max_length=2, blank=True, null=True)
    order_id = models.BigIntegerField(blank=True, null=True)
    menu_code = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_menu'


class SysMenuCopy(models.Model):
    menu_id = models.CharField(primary_key=True, max_length=100)
    menu_pid = models.CharField(max_length=100, blank=True, null=True)
    menu_text = models.CharField(max_length=100)
    role_id = models.CharField(max_length=100, blank=True, null=True)
    menu_url = models.CharField(max_length=100)
    menu_icon = models.CharField(max_length=100, blank=True, null=True)
    statu = models.IntegerField(blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    menu_icon_css = models.CharField(max_length=20, blank=True, null=True)
    menu_dot = models.CharField(max_length=2, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_menu_copy'


class SysParam(models.Model):
    sys_param_id = models.CharField(primary_key=True, max_length=100)
    param_name = models.CharField(max_length=100, blank=True, null=True)
    param_value = models.CharField(max_length=1000, blank=True, null=True)
    notes = models.CharField(max_length=100, blank=True, null=True)
    hospital_code = models.CharField(max_length=255, blank=True, null=True)
    sys_project_id = models.IntegerField(blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_param'


class SysTemplate(models.Model):
    sys_template_id = models.CharField(primary_key=True, max_length=100)
    template_content = models.TextField(blank=True, null=True)
    template_name = models.CharField(unique=True, max_length=255, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField(blank=True, null=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_template'


class SysToken(models.Model):
    sys_token_id = models.CharField(primary_key=True, max_length=50)
    token = models.CharField(max_length=200, blank=True, null=True)
    token_apply_domain = models.CharField(max_length=2, blank=True, null=True)
    token_desc = models.CharField(max_length=500, blank=True, null=True)
    token_statu = models.CharField(max_length=2, blank=True, null=True)
    token_expire = models.DateTimeField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    add_user = models.CharField(max_length=50, blank=True, null=True)
    token_apply_type = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_token'


class SysTokenBusiness(models.Model):
    sys_token_business_id = models.CharField(primary_key=True, max_length=50)
    sys_token_id = models.CharField(max_length=50, blank=True, null=True)
    business_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sys_token_business'


class UiControl(models.Model):
    rule_id = models.AutoField(primary_key=True)
    name_space = models.CharField(max_length=50)
    rule_name = models.CharField(max_length=50)
    rule_expression = models.CharField(max_length=255, blank=True, null=True)
    js = models.TextField(blank=True, null=True)
    exec_order = models.IntegerField(blank=True, null=True)
    css = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ui_control'
        unique_together = (('name_space', 'rule_name', 'rule_expression'),)


class UserAccount(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100)
    ladp_user_login_id = models.CharField(max_length=100, blank=True, null=True)
    role_id = models.CharField(max_length=255)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    user_pwd = models.CharField(max_length=100)
    last_login_ip = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    nick = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    email2 = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField()
    last_login_failure_time = models.DateTimeField(blank=True, null=True)
    login_failure_count = models.IntegerField(blank=True, null=True)
    avatar = models.TextField(blank=True, null=True)
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    jobtitle = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    department_arch = models.CharField(max_length=50, blank=True, null=True)
    not_in_leave = models.CharField(max_length=5, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    login_time = models.DateTimeField(blank=True, null=True)
    work_code = models.CharField(max_length=50, blank=True, null=True)
    hrm_department_id = models.CharField(max_length=50, blank=True, null=True)
    hrm_jobtitle_id = models.CharField(max_length=10, blank=True, null=True)
    user_hrm_department_id_level3 = models.CharField(max_length=50, blank=True, null=True)
    user_hrm_department_name_level3 = models.CharField(max_length=100, blank=True, null=True)
    entry_date = models.DateField(blank=True, null=True)
    department_id_level3_op_user = models.IntegerField(blank=True, null=True)
    leave_date = models.DateField(blank=True, null=True)
    last_mod_date = models.DateField(blank=True, null=True)
    hrm_locations_id = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    manager_id = models.CharField(max_length=50, blank=True, null=True)
    start_work_date = models.DateTimeField(blank=True, null=True)
    certificate_num = models.CharField(max_length=50, blank=True, null=True)
    bank_card_numbers = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    user_bank_card_id = models.CharField(max_length=50, blank=True, null=True)
    hrm_jobtitle_level = models.CharField(max_length=50, blank=True, null=True)
    skill = models.TextField(blank=True, null=True)
    dingtalk_user_id = models.CharField(max_length=80, blank=True, null=True)
    user_ldap_pwd = models.CharField(max_length=80, blank=True, null=True)
    it_authorization = models.CharField(max_length=5, blank=True, null=True)
    it_work_year = models.CharField(max_length=5, blank=True, null=True)
    education_background = models.CharField(max_length=50, blank=True, null=True)
    graduate_school = models.CharField(max_length=100, blank=True, null=True)
    graduation_time = models.DateField(blank=True, null=True)
    social_working_year = models.CharField(max_length=10, blank=True, null=True)
    it_work_start_time = models.DateField(blank=True, null=True)
    social_working_start_time = models.DateField(blank=True, null=True)
    reasons_leaving = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    regular_date = models.DateField(blank=True, null=True)
    phone_subsidy = models.CharField(max_length=50, blank=True, null=True)
    corp_code = models.CharField(max_length=50, blank=True, null=True)
    apply_card_no = models.CharField(max_length=255, blank=True, null=True)
    user_hrm_department_id_level2 = models.CharField(max_length=50, blank=True, null=True)
    salary_end_date = models.DateField(blank=True, null=True)
    city_id = models.CharField(max_length=50, blank=True, null=True)
    native_place = models.CharField(max_length=100, blank=True, null=True)
    is_marriage = models.CharField(max_length=50, blank=True, null=True)
    home_contact = models.CharField(max_length=50, blank=True, null=True)
    contact_relationship = models.CharField(max_length=50, blank=True, null=True)
    home_phone = models.CharField(max_length=50, blank=True, null=True)
    home_address = models.CharField(max_length=255, blank=True, null=True)
    education_form = models.CharField(max_length=50, blank=True, null=True)
    university_professional = models.CharField(max_length=50, blank=True, null=True)
    having_certificate = models.CharField(max_length=50, blank=True, null=True)
    person_resume = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_account'


class UserAccountCopy(models.Model):
    user_id = models.CharField(primary_key=True, max_length=100)
    ladp_user_login_id = models.CharField(max_length=100, blank=True, null=True)
    role_id = models.CharField(max_length=255)
    user_name = models.CharField(max_length=100, blank=True, null=True)
    user_pwd = models.CharField(max_length=100)
    last_login_ip = models.CharField(max_length=200, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    nick = models.CharField(max_length=100, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    email2 = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField()
    last_login_failure_time = models.DateTimeField(blank=True, null=True)
    login_failure_count = models.IntegerField(blank=True, null=True)
    avatar = models.TextField(blank=True, null=True)
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    jobtitle = models.CharField(max_length=50, blank=True, null=True)
    department = models.CharField(max_length=50, blank=True, null=True)
    department_arch = models.CharField(max_length=50, blank=True, null=True)
    not_in_leave = models.CharField(max_length=5, blank=True, null=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    login_time = models.DateTimeField(blank=True, null=True)
    work_code = models.CharField(max_length=50, blank=True, null=True)
    hrm_department_id = models.CharField(max_length=50, blank=True, null=True)
    hrm_jobtitle_id = models.CharField(max_length=10, blank=True, null=True)
    user_hrm_department_id_level3 = models.CharField(max_length=50, blank=True, null=True)
    user_hrm_department_name_level3 = models.CharField(max_length=100, blank=True, null=True)
    entry_date = models.DateField(blank=True, null=True)
    department_id_level3_op_user = models.IntegerField(blank=True, null=True)
    leave_date = models.DateField(blank=True, null=True)
    last_mod_date = models.DateField(blank=True, null=True)
    hrm_locations_id = models.CharField(max_length=50, blank=True, null=True)
    sex = models.CharField(max_length=2, blank=True, null=True)
    manager_id = models.CharField(max_length=50, blank=True, null=True)
    start_work_date = models.DateTimeField(blank=True, null=True)
    certificate_num = models.CharField(max_length=50, blank=True, null=True)
    bank_card_numbers = models.CharField(max_length=50, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    user_bank_card_id = models.CharField(max_length=50, blank=True, null=True)
    hrm_jobtitle_level = models.CharField(max_length=50, blank=True, null=True)
    skill = models.TextField(blank=True, null=True)
    dingtalk_user_id = models.CharField(max_length=80, blank=True, null=True)
    user_ldap_pwd = models.CharField(max_length=80, blank=True, null=True)
    it_authorization = models.CharField(max_length=5, blank=True, null=True)
    it_work_year = models.CharField(max_length=5, blank=True, null=True)
    education_background = models.CharField(max_length=50, blank=True, null=True)
    graduate_school = models.CharField(max_length=100, blank=True, null=True)
    graduation_time = models.DateField(blank=True, null=True)
    social_working_year = models.CharField(max_length=10, blank=True, null=True)
    it_work_start_time = models.DateField(blank=True, null=True)
    social_working_start_time = models.DateField(blank=True, null=True)
    reasons_leaving = models.TextField(blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)
    regular_date = models.DateField(blank=True, null=True)
    phone_subsidy = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_account_copy'


class UserAttendanceTravel(models.Model):
    user_attendance_travel_id = models.CharField(primary_key=True, max_length=50)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    hrm_department_id = models.CharField(max_length=5, blank=True, null=True)
    project_id = models.CharField(max_length=200, blank=True, null=True)
    begtime = models.DateField(blank=True, null=True)
    endtime = models.DateField(blank=True, null=True)
    beg_ampm = models.CharField(max_length=2, blank=True, null=True)
    end_ampm = models.CharField(max_length=2, blank=True, null=True)
    days = models.FloatField(blank=True, null=True)
    attendance_type = models.CharField(max_length=3, blank=True, null=True)
    req_time = models.DateTimeField(blank=True, null=True)
    req_end_time = models.DateTimeField(blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    wf_no = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_attendance_travel'


class UserBankCard(models.Model):
    user_bank_card_id = models.CharField(db_column='user_bank card_id', primary_key=True, max_length=50)  # Field renamed to remove unsuitable characters.
    user_id = models.CharField(max_length=50, blank=True, null=True)
    user_bank_card_name = models.CharField(db_column='user_bank card_name', max_length=50, blank=True, null=True)  # Field renamed to remove unsuitable characters.
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_bank_card'


class UserGroup(models.Model):
    user_group_id = models.CharField(primary_key=True, max_length=100)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=225, blank=True, null=True)
    user_group_name = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group'


class UserGroupRel(models.Model):
    user_id = models.CharField(max_length=100, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    modify_time = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=225, blank=True, null=True)
    user_group_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_group_rel'


class UserRole(models.Model):
    role_des = models.CharField(max_length=255, blank=True, null=True)
    role_id = models.CharField(primary_key=True, max_length=255)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    role_auth_level = models.IntegerField(blank=True, null=True)
    role_code = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_role'


class UserRoleEnv(models.Model):
    role_id = models.CharField(max_length=255)
    env_code = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_role_env'


class UserRoleFunc(models.Model):
    role_id = models.CharField(max_length=255)
    func_id = models.CharField(max_length=255)
    env_id = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)
    comments = models.CharField(max_length=225, blank=True, null=True)
    user_role_func_id = models.CharField(primary_key=True, max_length=50)
    menu_id = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'user_role_func'


class UserRoleIdList(models.Model):
    user_id = models.CharField(max_length=100, blank=True, null=True)
    role_id = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    order_weight = models.IntegerField(blank=True, null=True)
    role_list_id = models.IntegerField(blank=True, null=True)
    user_group_id = models.CharField(max_length=100, blank=True, null=True)
    user_role_type = models.CharField(max_length=2, blank=True, null=True)
    user_role_id_list_id = models.CharField(primary_key=True, max_length=50)

    class Meta:
        managed = False
        db_table = 'user_role_id_list'


class UserRoleInterface(models.Model):
    user_role_interface_id = models.CharField(primary_key=True, max_length=50)
    interface_name = models.CharField(max_length=100)
    interface_text = models.CharField(max_length=50, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_role_interface'


class UserRoleInterfaceLimit(models.Model):
    user_role_interface_limit_id = models.CharField(primary_key=True, max_length=50)
    user_role_interface_id = models.CharField(max_length=50, blank=True, null=True)
    interface_autho_cond = models.CharField(max_length=50, blank=True, null=True)
    interface_autho_type = models.CharField(max_length=50, blank=True, null=True)
    comments = models.CharField(max_length=255, blank=True, null=True)
    create_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_role_interface_limit'


class UserRoleInterfaceRel(models.Model):
    user_role_interface_rel_id = models.CharField(primary_key=True, max_length=50)
    role_id = models.CharField(max_length=255, blank=True, null=True)
    user_role_interface_id = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_role_interface_rel'


class UserRoleMenu(models.Model):
    role_id = models.CharField(max_length=255)
    menu_id = models.CharField(max_length=255)
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)
    user_role_menu_id = models.CharField(primary_key=True, max_length=50)
    sys_project_id = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_role_menu'


class UserTmp(models.Model):
    work_code = models.CharField(max_length=10, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)
    lastname = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_tmp'


class UserVacation(models.Model):
    user_vacation_id = models.CharField(primary_key=True, max_length=50)
    user = models.ForeignKey(UserAccount, models.DO_NOTHING)
    days = models.DecimalField(max_digits=4, decimal_places=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_vacation'


class UserVacationUseLog(models.Model):
    user_vacation_use_log_id = models.CharField(max_length=50, blank=True, null=True)
    user_vacation_id = models.CharField(max_length=50, blank=True, null=True)
    use_days = models.FloatField(blank=True, null=True)
    oa_flow_id = models.CharField(max_length=50, blank=True, null=True)
    add_time = models.DateTimeField(blank=True, null=True)
    comment = models.CharField(max_length=500, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    op_user = models.CharField(max_length=255, blank=True, null=True)
    current_days = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_vacation_use_log'


class UsersGroups(models.Model):
    user_id = models.IntegerField()
    group_id = models.IntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_groups'
        unique_together = (('user_id', 'group_id'),)


class UsersPermissions(models.Model):
    user_id = models.IntegerField()
    permission_id = models.IntegerField()
    create_time = models.DateTimeField()
    modify_time = models.DateTimeField()
    comments = models.CharField(max_length=225, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'users_permissions'
        unique_together = (('user_id', 'permission_id'),)


class WeekdaysHolidays(models.Model):
    date = models.DateField(primary_key=True)
    type = models.IntegerField(blank=True, null=True)
    festival_name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'weekdays_holidays'
