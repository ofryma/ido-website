import React, { createContext, useContext, ReactNode } from "react";
import { FileArray } from "chonky";
import { UploadFile } from "antd";

interface FileNavigContextType {
  files: FileArray;
  currentPath: string;
  inRootPath: boolean;
  navigateTo: (folderPath: string) => void;
  goBack: () => void;
  refreshFiles: () => void;
  uploadFileToS3: (file: File | UploadFile) => Promise<void>;
  deleteFileFromS3: (fileName: string) => Promise<void>;
}

const FileNavigContext = createContext<FileNavigContextType | null>(null);

interface FileNavigProviderProps {
  children: ReactNode;
}

export const FileNavigProvider: React.FC<FileNavigProviderProps> = ({ children }) => {
  return (
    <></>
  );
};

export const useFileNavigation = (): FileNavigContextType => {
  const context = useContext(FileNavigContext);
  if (!context) {
    throw new Error("useFileNavigation must be used within a FileNavigProvider");
  }
  return context;
};
