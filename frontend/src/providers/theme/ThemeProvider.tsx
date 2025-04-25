// frontend/src/providers/theme/ThemeProvider.tsx
import React, { createContext, useContext, useState, useEffect, ReactNode } from "react";
import { ThemeConfig } from 'antd';
import { lightTheme, darkTheme } from '../../styles/theme';

// Custom ThemeConfig with required token and additional tokens
interface CustomThemeConfig extends ThemeConfig {
  token: {
    colorPrimary: string;
    colorBgBase: string;
    colorTextBase: string;
    colorBorder: string;
    borderRadius: number;
    colorError: string; // Added for ChonkyDrive
    colorFooter: string; // Added for Footer
    colorHeaderBg: string; // Added for TopNavbar
    colorHeaderText: string; // Added for TopNavbar
  };
}

type ThemeMode = "light" | "dark";
interface ThemeContextType {
  themeMode: ThemeMode;
  changeThemeMode: () => void; // Renamed from toggleTheme
  theme: CustomThemeConfig; // Ant Design theme
  currentTheme: typeof lightTheme | typeof darkTheme; // Custom theme
}

const ThemeContext = createContext<ThemeContextType | undefined>(undefined);

const lightThemeConfig: CustomThemeConfig = {
  token: {
    colorPrimary: '#3b82f6',
    colorBgBase: '#f8fafc',
    colorTextBase: '#1e293b',
    colorBorder: '#e2e8f0',
    borderRadius: 8,
    colorError: '#ff4d4f', // Added for ChonkyDrive
    colorFooter: '#64748b', // Added for Footer
    colorHeaderBg: '#ffffff', // Added for TopNavbar
    colorHeaderText: '#1e293b', // Added for TopNavbar
  },
};

const darkThemeConfig: CustomThemeConfig = {
  token: {
    colorPrimary: '#60a5fa',
    colorBgBase: '#1e293b',
    colorTextBase: '#f8fafc',
    colorBorder: '#475569',
    borderRadius: 8,
    colorError: '#f5222d', // Added for ChonkyDrive
    colorFooter: '#94a3b8', // Added for Footer
    colorHeaderBg: '#334155', // Added for TopNavbar
    colorHeaderText: '#f8fafc', // Added for TopNavbar
  },
};

export const ThemeProvider: React.FC<{ children: ReactNode }> = ({ children }) => {
  const [themeMode, setThemeMode] = useState<ThemeMode>("light");

  useEffect(() => {
    const savedTheme = localStorage.getItem("themeMode") as ThemeMode | null;
    if (savedTheme) {
      setThemeMode(savedTheme);
    }
  }, []);

  const changeThemeMode = () => {
    const newMode = themeMode === "light" ? "dark" : "light";
    setThemeMode(newMode);
    localStorage.setItem("themeMode", newMode);
  };

  const theme = themeMode === "light" ? lightThemeConfig : darkThemeConfig;
  const currentTheme = themeMode === "light" ? lightTheme : darkTheme;

  return (
    <ThemeContext.Provider value={{ themeMode, changeThemeMode, theme, currentTheme }}>
      {children}
    </ThemeContext.Provider>
  );
};

export const useTheme = () => {
  const context = useContext(ThemeContext);
  if (!context) {
    throw new Error("useTheme must be used within a ThemeProvider");
  }
  return context;
};