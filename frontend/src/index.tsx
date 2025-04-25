import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';

import { OpenAPI as APIOpenAPI } from './api';
import { OpenAPI as AUTHOpenAPI } from './auth';
import { AuthProvider } from './providers/auth/AuthProvider';
import { ThemeProvider } from './providers/theme/ThemeProvider';


APIOpenAPI.BASE = `${process.env.REACT_APP_BACKEND_BASE_URL || ""}${APIOpenAPI.BASE}`
console.log("API Base URL", APIOpenAPI.BASE)
AUTHOpenAPI.BASE = `${process.env.REACT_APP_BACKEND_BASE_URL || ""}${AUTHOpenAPI.BASE}`
console.log("AUTH Base URL", AUTHOpenAPI.BASE)

const root = ReactDOM.createRoot(
  document.getElementById('root') as HTMLElement
);
root.render(

  <React.StrictMode>
    <ThemeProvider>
      <AuthProvider>
        <App />
      </AuthProvider>
    </ThemeProvider>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
