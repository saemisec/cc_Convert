# مدل‌های جدید ایجاد شده برای سیستم مدیریت تقاضا و قرارداد

## مدل‌های ایجاد شده:

### 1. **Demand** (تقاضا)

- `id`: شناسه اصلی
- `code`: کد تقاضا (با ایندکس)
- `title`: عنوان تقاضا
- روابط: `project_demands` (یک به چند)

### 2. **Workflow** (گردش کار)

- `id`: شناسه اصلی
- `title`: عنوان گردش کار
- روابط: `workflow_details`, `project_demands`

### 3. **Project_demand_stage** (مرحله تقاضای پروژه)

- `id`: شناسه اصلی
- `title`: عنوان مرحله
- روابط: `workflow_details_from`, `workflow_details_to` (با foreign_keys جداگانه)

### 4. **Workflow_detail** (جزئیات گردش کار)

- `id`: شناسه اصلی
- `workflow_id`: شناسه گردش کار
- `prev_id`: شناسه مرحله قبلی (self-referencing)
- `from_stage_id`: شناسه مرحله مبدا
- `to_stage_id`: شناسه مرحله مقصد
- روابط: `workflow`, `prev_detail`, `from_stage`, `to_stage`

### 5. **Demand_document_type** (نوع سند تقاضا)

- `id`: شناسه اصلی با `Identity(always=True)`
- `title`: عنوان نوع سند (با `UniqueConstraint`)
- روابط: `demand_documents`
- ****table_args****: `UniqueConstraint("title")`

### 6. **Demand_document** (سند تقاضا)

- `id`: شناسه اصلی با `Identity(always=True)`
- `title`: عنوان سند
- `document_type_id`: شناسه نوع سند
- روابط: `document_type`, `project_demand_details`, `purchase_request`, `tender`, `bidder`, `bidders_document`, `inquery`, `tbe_request` (همه یک به یک به جز project_demand_details)

### 7. **Purchase_request** (درخواست خرید)

- `id`: کلید خارجی به `demand_document.id` (یک به یک)
- `title`: عنوان درخواست خرید
- `issue_date`: تاریخ صدور
- `sec_phase_id`: شناسه فاز دوم (با ایندکس)
- `main_project_id`: شناسه پروژه اصلی (با ایندکس)
- `supply_method`: روش تامین (nullable)
- روابط: `demand_document`, `second_phase`, `main_project`
- ****table_args****: `Index` ترکیبی برای `sec_phase_id` و `issue_date`، `Index` برای `main_project_id`

### 8. **Tender** (مناقصه)

- `id`: کلید خارجی به `demand_document.id` (یک به یک)
- `title`: عنوان مناقصه
- `project_id`: شناسه پروژه (با ایندکس)
- `issue_date`: تاریخ صدور
- `winner_id`: شناسه برنده (nullable، با ایندکس)
- `status`: وضعیت مناقصه (Enum: NOT_START, INVITATION, TBE_REQUEST, BID_WINNER, FINAL)
- `has_spare_part`: دارای قطعات یدکی
- `has_extra_cost`: دارای هزینه اضافی
- روابط: `demand_document`, `main_project`, `winner` (Partner)، `bidders`, `tbe_requests`
- ****table_args****: `Index` ترکیبی برای `project_id` و `issue_date`، `Index` برای `status`

### 9. **Bidder** (مناقصه‌گر)

- `id`: کلید خارجی به `demand_document.id` (یک به یک)
- `tender_id`: شناسه مناقصه (با ایندکس)
- `partner_id`: شناسه شریک/پیمانکار (با ایندکس)
- روابط: `demand_document`, `tender`, `partner`, `bidder_documents`
- ****table_args****: `Index` ترکیبی برای `tender_id` و `partner_id`

### 10. **Bidders_Document** (اسناد مناقصه‌گر)

- `id`: کلید خارجی به `demand_document.id` (یک به یک)
- `bidder_id`: شناسه مناقصه‌گر (با ایندکس)
- `doc_title`: عنوان سند
- `doc_path`: مسیر سند
- `doc_type`: نوع سند
- روابط: `demand_document`, `bidder`
- ****table_args****: `Index` برای `bidder_id`

### 11. **Inquery** (استعلام)

- `id`: کلید خارجی به `demand_document.id` (یک به یک)
- `title`: عنوان استعلام
- `project_id`: شناسه پروژه (با ایندکس)
- `partner_id`: شناسه شریک (با ایندکس)
- `inquery_no`: شماره استعلام (با `UniqueConstraint`)
- `status`: وضعیت استعلام (Enum: PENDING, DELETE, FINAL)
- روابط: `demand_document`, `main_project`, `partner`
- ****table_args****: `UniqueConstraint("inquery_no")`, `Index` ترکیبی برای `project_id` و `partner_id`، `Index` برای `status`

### 12. **TBE_Request** (درخواست TBE)

- `id`: کلید خارجی به `demand_document.id` (یک به یک)
- `project_id`: شناسه پروژه (با ایندکس)
- `issue_date`: تاریخ صدور
- `tender_id`: شناسه مناقصه (با ایندکس)
- `tbe_id`: شناسه MDR (با ایندکس)
- روابط: `demand_document`, `main_project`, `tender`, `mdr`
- ****table_args****: `Index` ترکیبی برای `project_id` و `issue_date`، `Index` برای `tender_id`

### 13. **Project_demand** (تقاضای پروژه) - _بازنویسی شده_

- `id`: شناسه اصلی
- `project_id`: شناسه پروژه (با ایندکس)
- `demand_id`: شناسه تقاضا (با ایندکس)
- `workflow_id`: شناسه گردش کار (با ایندکس)
- `qty`: تعداد
- روابط: `project`, `demand`, `workflow`, `project_demand_details`, `contract_items`

### 14. **Project_demand_details** (جزئیات تقاضای پروژه)

- `id`: شناسه اصلی
- `qty`: تعداد (float)
- `project_demand_id`: شناسه تقاضای پروژه (با ایندکس)
- `issue_date`: تاریخ صدور
- `demand_document_id`: شناسه سند تقاضا (با ایندکس)
- روابط: `project_demand`, `demand_document`

### 15. **Statement_items** (اقلام صورت وضعیت)

- `id`: شناسه اصلی
- `statement_id`: شناسه صورت وضعیت (با ایندکس)
- `contract_item_id`: شناسه قلم قرارداد (با ایندکس)
- `qty`: تعداد
- روابط: `statement`, `contract_item`

## مدل‌های موجود که آپدیت شدند:

### 1. **Main_project**

روابط اضافه شده:

- `project_demands`: به `Project_demand`
- `purchase_requests`: به `Purchase_request`
- `tenders`: به `Tender`
- `inqueries`: به `Inquery`
- `tbe_requests`: به `TBE_Request`

**نکته**: نسخه‌بندی پروژه از طریق `main_addendum` مدیریت می‌شود

### 2. **Pre_contract**

**نکته**: نسخه‌بندی قرارداد از طریق `addendum` مدیریت می‌شود

### 3. **Contract_item**

فیلدها و روابط اضافه شده:

- `project_demand_id`: شناسه تقاضای پروژه (nullable)
- `project_demand`: به `Project_demand`
- `statement_items`: به `Statement_items`

### 4. **Statement**

روابط اضافه شده:

- `statement_items`: به `Statement_items`

### 5. **Partner**

روابط اضافه شده:

- `won_tenders`: به `Tender` (مناقصاتی که برنده شده)
- `bidders`: به `Bidder` (مناقصاتی که شرکت کرده)
- `inqueries`: به `Inquery` (استعلامات)

### 6. **Mdr**

روابط اضافه شده:

- `tbe_requests`: به `TBE_Request`

### 7. **Second_Phase**

روابط اضافه شده:

- `purchase_requests`: به `Purchase_request`

## ویژگی‌های پیاده‌سازی:

✅ **استاندارد جدید Primary Key**: `id: Mapped[int] = mapped_column(Identity(always=True), primary_key=True, index=True)`  
✅ **Primary Key با Foreign Key** (برای روابط یک به یک): `id: Mapped[int] = mapped_column(ForeignKey("parent_table.id"), primary_key=True, index=True)`  
✅ همه foreign keys با `index=True`  
✅ همه relationships دوطرفه با `back_populates`  
✅ Self-referencing در `Workflow_detail` با `remote_side`  
✅ Multiple relationships به یک مدل با `foreign_keys` مشخص  
✅ استفاده از `__table_args__` برای `UniqueConstraint` و `Index` ترکیبی  
✅ استفاده از `Enum` برای فیلدهای با مقادیر محدود (مانند `status`)  
✅ همه مدل‌ها به `models/__init__.py` اضافه شدند  
✅ تمام imports در `__all__` به‌روزرسانی شد

## الگوهای طراحی به کار رفته:

### 1. **رابطه یک به یک با استفاده از Foreign Key در Primary Key**

مدل‌های `Purchase_request`، `Tender`، `Bidder`، `Bidders_Document`، `Inquery` و `TBE_Request` همگی از `Demand_document` به عنوان جدول والد استفاده می‌کنند و `id` آن‌ها هم کلید اصلی و هم کلید خارجی است.

```python
id: Mapped[int] = mapped_column(
    ForeignKey("demand_document.id"), primary_key=True, index=True
)
```

### 2. **Enum برای مدیریت وضعیت‌ها**

```python
class Tender_status(enum.Enum):
    NOT_START = "شروع نشده"
    INVITATION = "دعوت"
    TBE_REQUEST = "درخواست TBE"
    BID_WINNER = "برنده مناقصه"
    FINAL = "نهایی"
```

### 3. **Index ترکیبی برای بهینه‌سازی Query**

```python
__table_args__ = (
    Index("idx_purchase_request_phase_date", "sec_phase_id", "issue_date"),
    Index("idx_purchase_request_project", "main_project_id"),
)
```

### 4. **UniqueConstraint برای جلوگیری از داده تکراری**

```python
__table_args__ = (
    UniqueConstraint("inquery_no", name="uq_inquery_no"),
)
```

## نکات مهم:

1. مدل `Project_demand` قبلی که برای stuff/MR بود، کاملاً بازنویسی شد
2. تمام روابط طبق دیاگرام ER شما پیاده‌سازی شدند
3. ایندکس‌ها روی تمام foreign key ها اعمال شده
4. nullable fields در جاهای مناسب تعریف شدند (مثل `prev_id` در Workflow_detail، `winner_id` در Tender)
5. **استاندارد جدید**: استفاده از `Identity(always=True)` به جای `autoincrement=True` برای کلیدهای اصلی
6. روابط یک به یک با `uselist=False` مشخص شده‌اند
7. در `Partner` از `foreign_keys` برای تفکیک روابط مختلف به `Tender` استفاده شده

## مراحل بعدی:

1. ایجاد migration با Alembic:

   ```bash
   cd cc_backend
   alembic revision --autogenerate -m "Add purchase_request, tender, bidder, inquery, tbe_request models with Identity"
   alembic upgrade head
   ```

2. ایجاد operations برای هر entity (router, service, schema, crud)

## ساختار سلسله‌مراتبی مدل‌ها:

```
Demand_document (هسته مرکزی)
├── Purchase_request (درخواست خرید)
├── Tender (مناقصه)
│   ├── Bidder (مناقصه‌گر)
│   │   └── Bidders_Document (اسناد مناقصه‌گر)
│   └── TBE_Request (درخواست TBE)
└── Inquery (استعلام)
```
