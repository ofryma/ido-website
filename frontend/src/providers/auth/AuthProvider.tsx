import React, { createContext, useContext, useState, useEffect, ReactNode } from "react";
import { DefaultService } from "../../auth";

interface User {}

interface AuthContextType {
  user: User | null;
  login: (username: string, password: string) => void;
  logout: () => void;
  isValid: boolean;
  validateSession: () => void;
}

const AuthContext = createContext<AuthContextType | null>(null);

interface AuthProviderProps {
  children: ReactNode;
}

export const AuthProvider: React.FC<AuthProviderProps> = ({ children }) => {
  const [user, setUser] = useState<User | null>(null);
  const [isValid, setIsValid] = useState<boolean>(false);

  useEffect(() => {
    validateSession();
  }, [user]);

  const login = async (username: string, password: string) => {
    await DefaultService.loginLoginPost(
      username,
      password
    );
  };

  const logout = async () => {

    await DefaultService.logoutLogoutPost();
    validateSession();
    setUser(null);
  };

  const validateSession = async () => {
    try {
      await DefaultService.validateAccessTokenValidateTokenPost();
      setIsValid(true);
    } catch (error) {
      setIsValid(false);
    }
  }

  return (
    <AuthContext.Provider value={{ user, login, logout, isValid , validateSession }}>
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = (): AuthContextType => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error("useAuth must be used within an AuthProvider");
  }
  return context;
};