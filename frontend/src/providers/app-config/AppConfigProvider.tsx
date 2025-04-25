import React, { createContext, useContext, ReactNode } from "react";

interface AppConfigContextType {
    companyName: string;
    baseUrl: string;
}

const AppConfigContext = createContext<AppConfigContextType | null>(null);

interface AppConfigProviderProps {
    children: ReactNode;
}

export const AppConfigProvider: React.FC<AppConfigProviderProps> = ({ children }) => {
    
    const companyName : string = process.env.REACT_APP_COMPANY_NAME || "APP_NAME";
    const baseUrl: string = process.env.REACT_APP_BASE_URL || `${window.location.origin}/facerek`;

    return (
        <AppConfigContext.Provider value={{ companyName , baseUrl }}>
            {children}
        </AppConfigContext.Provider>
    );
};

export const useAppConfig = (): AppConfigContextType => {
    const context = useContext(AppConfigContext);
    if (!context) {
        throw new Error("useAppConfig must be used within an AppConfigProvider");
    }
    return context;
};