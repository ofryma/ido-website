// frontend/src/App.tsx
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import HomePage from "./pages/HomePage";
import { ConfigProvider } from 'antd';
import { SwitchThemeButton } from "./components/buttons/SwitchThemeButton";
import { useTheme } from "./providers/theme/ThemeProvider";
import { AppConfigProvider } from "./providers/app-config/AppConfigProvider";
import { ThemeProvider } from "./providers/theme/ThemeProvider"; // Add this
import { ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { OpenAPI } from "./api";
import { Accessibility } from 'accessibility';
import { useEffect } from "react";


OpenAPI.BASE = `${process.env.REACT_APP_API_ENDPOINT}${OpenAPI.BASE}`;

function App() {
  
  const { theme } = useTheme();

  useEffect(() => {
    window.addEventListener('load', function() { new Accessibility(); }, false);
  }, []);

  return (
    <ThemeProvider> {/* Wrap with ThemeProvider */}
      <ConfigProvider theme={theme}>
        <AppConfigProvider>
          <ToastContainer
            position="top-center"
            autoClose={5000}
            stacked={true}
            toastStyle={{
              backgroundColor: theme.token.colorBgBase,
              color: theme.token.colorTextBase, // Updated to colorTextBase
            }}
          />
          <Router basename="/">
            <Routes>
              <Route path="/" element={<HomePage />} />
            </Routes>
            {/* <SwitchThemeButton /> */}
          </Router>
        </AppConfigProvider>
      </ConfigProvider>
    </ThemeProvider>
  );
}

export default App;