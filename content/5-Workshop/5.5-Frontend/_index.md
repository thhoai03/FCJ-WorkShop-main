---
title: "Connect Frontend"
date: 2026-07-21
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---#5. Connect React Frontend with Serverless Backend

Once the Backend is ready, the next step is to configure the Frontend so the React application knows how to call the APIs on AWS.

---

### Step 1: Declare environment variables

Open the `cake-shop-frontend` directory, find (or create a new) file named `.env` in the frontend root directory.

Add the following environment variable to the `.env` file, replacing the value `<ApiUrl from Outputs>` with the actual API Gateway URL you received after deploying the backend:

```env
VITE_API_URL=https://<api-id>.execute-api.ap-southeast-1.amazonaws.com/Prod/
```

### Step 2: Integrate API and Auth (Processing flow)

The Frontend needs to be programmed to interact with the Backend safely and correctly. Below is the main operational flow you need to establish in the `src/services/api.js` and `src/services/auth.js` files:

1. **Handle login and save Token:**
   After successfully calling the `/auth/login` API, the backend will return a JWT string (`idToken`). The Frontend needs to save this string into `localStorage` or a secure state management mechanism to use for subsequent requests.

2. **Call authenticated API (Admin Request):**
   Every HTTP request directed at administrator features (such as adding products, viewing orders) must attach the token to the header:
   ```javascript
   // Example of attaching header using axios or fetch
   headers: {
     'Authorization': idToken
   }
   ```
   If the API Gateway does not find this token (or the token doesn't belong to the `admin` group), it will automatically block the request and return a 401/403 error.

3. **Image Upload Mechanism:**
   The system does not send large image files directly through API Gateway and Lambda to avoid exceeding the payload limit (6 MB) and save computing costs.
   The image upload flow goes through 2 steps:
   - **Step 1:** The Frontend calls the `/uploads/presign` API to request a temporary "Pass" (a pre-signed secure URL).
   - **Step 2:** The Frontend uses the received `uploadUrl` to directly send the image file to **Amazon S3** via the HTTP `PUT` protocol.

---

### Step 3: Run the application

After finishing the `.env` configuration, open a terminal in the `cake-shop-frontend` directory and start the development server:

```bash
npm install
npm run dev
```

Now you can access `http://localhost:5173` in your browser. The React Frontend will display real data retrieved from DynamoDB via API Gateway, completing the HMN Bakery Online Cake Ordering system!