# Simple Warehouse Management

---

# Local Development

```bash
pip install -r requirements.txt
```

```bash
python manage.py migrate
```

```bash
python manage.py runserver
```

---

# Links

- This link is in an online dev environment and can be unstable, try to clone and test the code locally for better performance.

### Admin Login

- https://cuddly-fortnight.fly.dev/admin/

### Warehouse List

- https://cuddly-fortnight.fly.dev/warehouses/warehouse/

### Supplier List

- https://cuddly-fortnight.fly.dev/warehouses/suppliers/

### Product List

- https://cuddly-fortnight.fly.dev/warehouses/products/

### Customer List

- https://cuddly-fortnight.fly.dev/warehouses/customers/

## Reports

- https://cuddly-fortnight.fly.dev/reports/

---

## Testing Report

- [Click Here](https://github.com/animemoeus/cuddly-fortnight/issues/5)

---

## Technologies Stack

- BE: Django
- DB: Sqlite (since we use Django ORM, we can easily change to another database like MySQL or Postgres without changing the query.

---

## TODO:
- Add validation for outgoing warehouse transactions to prevent negative value in the box or pcs total.
- Create a custom form for the CRUD. Currently, this project is using default from from Django admin. Although the default form already handles all of our needs, consider using a custom form with a popular JavaScript library like React, etc with API for better UI/UX and performance.
