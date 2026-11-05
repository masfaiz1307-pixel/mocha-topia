# ☕ Mocha Topia — Complete API Documentation & Validation Guide

**Course:** Information Systems Agile Project Management with DevOps (ISAPMD) — Week 7  
**Class:** Information Systems 2026 (IS 2026)  
**Lecturer:** Eka Parima Saragih, S.Kom., M.Kom.  
**Deliverable Type:** API Documentation (Deliverable 2)  
**Platform Coverage:** OpenAPI 3.0.3, Swagger UI, Postman Collection v2.1  

---

## 👥 Group Identity & Metadata

| Field | Detail |
|---|---|
| **Group Number** | Group 04 |
| **Project Name** | Mocha Topia (Coffee Shop Web Application) |
| **Team Members & Student IDs** | 1. **Faiz** (`012202500030`)<br>2. **Immanuel** (`012202500017`)<br>3. **Dwisasono** (`012202500064`) |
| **Repository URL** | `https://github.com/masfaiz1307-pixel/mocha-topia` |
| **API Base URL** | `http://localhost:8080` (Docker Container Port 8080:80) |
| **External Integration** | FormSubmit AJAX API (`https://formsubmit.co/ajax/...`) |
| **OpenAPI Specification File** | [`openapi.yaml`](openapi.yaml) / [`openapi.json`](openapi.json) |
| **Interactive Documentation** | [`API_DOCUMENTATION.html`](API_DOCUMENTATION.html) |
| **Postman Test Collection** | [`MochaTopia_API_Postman_Collection.json`](MochaTopia_API_Postman_Collection.json) |

---

## 📑 Table of Contents
1. [API Architecture & Principles](#1-api-architecture--principles)
2. [HTTP Status Codes Reference (Week 7 PPT Slide 61)](#2-http-status-codes-reference)
3. [Authentication & Profile Endpoints](#3-authentication--profile-endpoints)
4. [Menu & Catalog Endpoints](#4-menu--catalog-endpoints)
5. [Shopping Cart Endpoints](#5-shopping-cart-endpoints)
6. [Orders & Checkout Endpoints (BUG-1042 Test)](#6-orders--checkout-endpoints)
7. [Contact & FormSubmit Integration](#7-contact--formsubmit-integration)
8. [System Health & DevOps Endpoint](#8-system-health--devops-endpoint)
9. [Postman Automated Validation Suite](#9-postman-automated-validation-suite)
10. [Traceability Matrix: Acceptance Criteria to API Test Evidence](#10-traceability-matrix)

---

## 1. API Architecture & Principles

The Mocha Topia API is built following RESTful constraints:
- **Stateless Communication:** Every request contains all context, authentication headers, and payload required for evaluation.
- **Resource-Oriented URIs:** Nouns represent business entities (`/api/v1/auth`, `/api/v1/menu`, `/api/v1/cart`, `/api/v1/orders`).
- **Standard HTTP Methods:**
  - `GET`: Retrieve resources without side effects.
  - `POST`: Create new resources or execute actions (registration, login, order placement).
  - `PUT`: Update existing resources (cart quantities).
  - `DELETE`: Remove resources (cart items or entire cart).
- **JSON Data Payloads:** All bodies use `Content-Type: application/json; charset=utf-8`.

---

## 2. HTTP Status Codes Reference

As taught in **Slide 61 of the ISAPMD Week 7 Lecture**, the Mocha Topia API consistently implements standardized HTTP status codes:

| Status Code | Meaning | Usage in Mocha Topia |
|---|---|---|
| **200 OK** | Request succeeded | Menu listing retrieved, user profile fetched, cart updated, login successful |
| **201 Created** | New resource created | New user registered, new order placed with receipt ID generated |
| **400 Bad Request** | Invalid/missing request data | Missing password, invalid email syntax, unselected payment method (BUG-1042) |
| **401 Unauthorized** | Authentication missing/invalid | Missing Bearer token on protected profile/order routes, wrong password |
| **403 Forbidden** | Authenticated user lacks permission | Requester attempts to retrieve another user's order receipt (Slide 71) |
| **404 Not Found** | Resource does not exist | Menu item ID not found (`/menu/9999`), invalid order ID |
| **409 Conflict** | Resource state conflict | Username or email already registered |
| **500 Server Error** | Unexpected server-side failure | Unhandled database or backend exception |

---

## 3. Authentication & Profile Endpoints

### 3.1 POST `/api/v1/auth/register`
Creates a new customer account with client and server schema verification.

**Request Headers:**
```http
Content-Type: application/json
```

**Request Body Schema:**
```json
{
  "username": "faiz_dev",
  "email": "faiz@mochatopia.com",
  "password": "CoffeePass123"
}
```

**Password Rules Verified:**
- Length >= 8 characters
- At least 1 uppercase letter (`[A-Z]`)
- At least 1 lowercase letter (`[a-z]`)
- At least 1 numeric digit (`[0-9]`)

**Success Response (`201 Created`):**
```json
{
  "status": "success",
  "message": "Account created successfully! ✓",
  "user": {
    "id": 101,
    "username": "faiz_dev",
    "email": "faiz@mochatopia.com"
  }
}
```

**Failure Response (`400 Bad Request`):**
```json
{
  "status": "error",
  "error": "Password does not meet complexity requirements. Must contain uppercase, lowercase, and numeric characters with minimum 8 characters."
}
```

---

### 3.2 POST `/api/v1/auth/login`
Authenticates user credentials and issues a JWT session token.

**Request Body:**
```json
{
  "username": "faiz_dev",
  "password": "CoffeePass123"
}
```

**Success Response (`200 OK`):**
```json
{
  "status": "success",
  "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMDEiLCJ1c2VybmFtZSI6ImZhaXpfZGV2In0...",
  "expiresIn": 3600,
  "user": {
    "username": "faiz_dev",
    "email": "faiz@mochatopia.com"
  }
}
```

**Failure Response (`401 Unauthorized`):**
```json
{
  "status": "error",
  "error": "Incorrect username or password!"
}
```

---

### 3.3 GET `/api/v1/auth/me`
Retrieves customer profile for active Bearer token.

**Request Headers:**
```http
Authorization: Bearer eyJhbGciOiJIUzI1Ni...
```

**Success Response (`200 OK`):**
```json
{
  "id": 101,
  "username": "faiz_dev",
  "email": "faiz@mochatopia.com",
  "createdAt": "2026-10-22T08:30:00Z"
}
```

---

## 4. Menu & Catalog Endpoints

### 4.1 GET `/api/v1/menu`
Retrieves the complete catalog of 12 beverages and food items.

**Query Parameters:**
| Parameter | Type | Required | Values | Description |
|---|---|---|---|---|
| `category` | String | No | `all`, `drink`, `food` | Filters items by category |
| `search` | String | No | Free text | Case-insensitive search keyword |

**Example Request:**
```bash
curl -X GET "http://localhost:8080/api/v1/menu?category=drink&search=americano"
```

**Success Response (`200 OK`):**
```json
[
  {
    "id": 1,
    "name": "Americano",
    "price": 20000,
    "img": "images/Americano.jpeg",
    "cat": "drink"
  }
]
```

---

### 4.2 GET `/api/v1/menu/{id}`
Returns details for a specific menu item.

**Path Parameter:** `id` (integer)

**Success Response (`200 OK`):**
```json
{
  "id": 2,
  "name": "Cappuccino",
  "price": 25000,
  "img": "images/cappucino.jpeg",
  "cat": "drink"
}
```

**Failure Response (`404 Not Found`):**
```json
{
  "status": "error",
  "error": "Menu item not found"
}
```

---

## 5. Shopping Cart Endpoints

### 5.1 GET `/api/v1/cart`
Returns active cart contents and calculated subtotals.

**Success Response (`200 OK`):**
```json
{
  "items": [
    {
      "name": "Americano",
      "price": 20000,
      "qty": 2,
      "img": "images/Americano.jpeg",
      "subtotal": 40000
    },
    {
      "name": "Sweet Buns",
      "price": 12000,
      "qty": 1,
      "img": "images/sweetbuns.jpeg",
      "subtotal": 12000
    }
  ],
  "totalCount": 3,
  "totalPrice": 52000,
  "formattedTotal": "Total: Rp 52.000"
}
```

---

### 5.2 POST `/api/v1/cart/items`
Adds an item with quantity (minimum 1) to cart.

**Request Body:**
```json
{
  "name": "Americano",
  "price": 20000,
  "qty": 2,
  "img": "images/Americano.jpeg"
}
```

---

### 5.3 DELETE `/api/v1/cart`
Clears all items in the active cart.

**Success Response (`200 OK`):**
```json
{
  "message": "Cart cleared successfully",
  "total": 0
}
```

---

## 6. Orders & Checkout Endpoints

### 6.1 POST `/api/v1/orders`
Submits checkout order. Validates all recipient information and payment method.

> **Crucial Lecture Bug Scenario (BUG-1042):**  
> If the `payment` method field is empty or unselected, the endpoint **MUST** reject the payload with `400 Bad Request` and return `"Payment method is required"`, preventing an application crash.

**Request Body (Valid Submission):**
```json
{
  "name": "Faiz Daffa",
  "phone": "081234567890",
  "address": "Jl. Sudirman No. 45, Jakarta Pusat",
  "payment": "Cash",
  "items": [
    {
      "name": "Americano",
      "price": 20000,
      "qty": 2
    },
    {
      "name": "Cheese Toast",
      "price": 16000,
      "qty": 1
    }
  ]
}
```

**Success Response (`201 Created`):**
```json
{
  "orderId": "ORD-2026-1022",
  "name": "Faiz Daffa",
  "phone": "081234567890",
  "address": "Jl. Sudirman No. 45, Jakarta Pusat",
  "payment": "Cash",
  "cart": [
    {"name": "Americano", "price": 20000, "qty": 2},
    {"name": "Cheese Toast", "price": 16000, "qty": 1}
  ],
  "total": 56000,
  "time": "10/22/2026, 9:30:15 AM",
  "status": "Confirmed"
}
```

**Negative Response (`400 Bad Request` - BUG-1042 test):**
```json
{
  "status": "error",
  "error": "Payment method is required. Please select Cash, QRIS, or Bank Transfer to proceed."
}
```

---

### 6.2 GET `/api/v1/orders/{orderId}`
Retrieves order receipt details. Enforces authorization checks as taught in **Slide 71**.

- **Valid Owner:** Returns `200 OK` with order receipt.
- **Unauthorized Requester (User B trying to view User A's order):** Returns `403 Forbidden` without exposing any order data.

---

## 7. Contact & FormSubmit Integration

### 7.1 POST `https://formsubmit.co/ajax/{recipientEmail}`
Integrated in `contact.html` for zero-server contact message delivery.

**Parameters:**
- `recipientEmail`: `masfaiz1307@gmail.com`

**Payload Data:**
```http
POST /ajax/masfaiz1307@gmail.com HTTP/1.1
Host: formsubmit.co
Content-Type: application/x-www-form-urlencoded
Accept: application/json

name=Faiz+Daffa&email=masfaiz1307%40gmail.com&phone=081234567890&topic=Feedback&visit_type=Dine+In&newsletter=Yes&message=Excellent+Arabica+espresso+today!&_subject=New+Contact+Form+Submission+-+Mocha+Topia&_captcha=false&_template=table&_autoresponse=Thank+you+for+contacting+Mocha+Topia!
```

**Success Response (`200 OK`):**
```json
{
  "success": "true",
  "message": "Form submitted successfully!"
}
```

---

## 8. System Health & DevOps Endpoint

### 8.1 GET `/healthz` (or `/` container root)
Checks that the Nginx Alpine container is actively running on port 8080.

```bash
curl.exe -I http://localhost:8080/
```

**Response:**
```http
HTTP/1.1 200 OK
Server: nginx/1.27.5
Content-Type: text/html
Connection: keep-alive
```

---

## 9. Postman Automated Validation Suite

Our Postman collection (`MochaTopia_API_Postman_Collection.json`) contains test assertion scripts written using the Postman sandbox (`pm.test`, `pm.expect`), directly implementing the test types highlighted in **Slide 69 of the Week 7 PPT**:

### 1. Status Code Verification Check
```javascript
pm.test("Status code is 201 Created", function () {
    pm.response.to.have.status(201);
});
```

### 2. Response Body Schema Check
```javascript
pm.test("Response has a generated order ID and valid total", function () {
    const body = pm.response.json();
    pm.expect(body.orderId).to.exist;
    pm.expect(body.total).to.be.a('number');
    pm.expect(body.status).to.eql('Confirmed');
});
```

### 3. Performance & Latency Check
```javascript
pm.test("Response time is below 1000 ms", function () {
    pm.expect(pm.response.responseTime).to.be.below(1000);
});
```

### 4. Content-Type Header Verification
```javascript
pm.test("Header Content-Type is application/json", function () {
    pm.expect(pm.response.headers.get("Content-Type")).to.include("application/json");
});
```

---

## 10. Traceability Matrix

Traceability from user stories to acceptance criteria, test cases, and release evidence (**Slide 72**):

| User Story | Acceptance Criteria | Test Scenario ID | API Endpoint | Verification Status |
|---|---|---|---|---|
| **US-01: User Registration** | Validates email syntax, username length >=3, password complexity | `MT-REG-001` - `025` | `POST /api/v1/auth/register` | ✅ **PASS** |
| **US-02: Authentication** | Rejects invalid password with 401; stores session on success | `MT-AUTH-001` - `025` | `POST /api/v1/auth/login` | ✅ **PASS** |
| **US-03: Menu Browsing** | Displays 12 items; filters by drink/food; case-insensitive search | `MT-MENU-001` - `025` | `GET /api/v1/menu` | ✅ **PASS** |
| **US-04: Item Modal** | Increment/decrement qty; clamps at minimum 1 | `MT-MOD-001` - `020` | `POST /api/v1/cart/items` | ✅ **PASS** |
| **US-05: Shopping Cart** | Calculates unit * qty; real-time total; clear cart prompt | `MT-CART-001` - `030` | `GET/DELETE /api/v1/cart` | ✅ **PASS** |
| **US-06: Checkout Order** | Validates recipient; requires payment method (BUG-1042 check) | `MT-CHK-001` - `025` | `POST /api/v1/orders` | ✅ **PASS** |
| **US-07: Contact Form** | Submits via FormSubmit AJAX; displays loading spinner and confirmation | `MT-CNT-001` - `025` | `POST /ajax/{email}` | ✅ **PASS** |
| **US-08: Container Health** | Nginx Alpine responds 200 OK on port 8080 with Gzip and headers | `MT-API-022` | `GET /` | ✅ **PASS** |

---

*Mocha Topia API Documentation — Prepared by Group 04 for ISAPMD Week 7 Submission.*
