import React, { createContext, useContext, useState, useEffect, ReactNode, useCallback } from "react";
import AWS from "aws-sdk";
import { FileArray, FileData } from "chonky";
import { useTheme } from "../../providers/theme/ThemeProvider";
import { toast } from "react-toastify";
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

  // const { theme } = useTheme();
  // const [s3Client, setS3Client] = useState<AWS.S3 | undefined>();
  // const [s3TokenResponse, setS3TokenResponse] = useState<S3TokenResponse | undefined>();
  // const [files, setFiles] = useState<FileArray>([]);
  // const [currentPath, setCurrentPath] = useState<string>("");
  // const [, setPathHistory] = useState<string[]>([]);

  // const inRootPath: boolean = s3TokenResponse?.access_key_id === currentPath || `${s3TokenResponse?.access_key_id}/` === currentPath;

  // useEffect(() => {
  //   const fetchS3Creds = async () => {
  //     try {
  //       const response = await ClientService.getS3TokenClientGetS3TokenPost();
  //       setS3TokenResponse(response);
  //     } catch (error) {
  //       console.error(error);

  //       // ********************************************************************************
  //       // Don't use this code part if not in development
  //       setS3TokenResponse(mockS3TokenResponse);
  //       // ********************************************************************************

  //     }
  //   };
  //   fetchS3Creds();
  // }, []);

  // useEffect(() => {
  //   if (!s3TokenResponse) return;

  //   AWS.config.update({
  //     region: s3TokenResponse.region,
  //     accessKeyId: s3TokenResponse.access_key_id,
  //     secretAccessKey: s3TokenResponse.secret_access_key,
  //     sessionToken: s3TokenResponse.session_token,
  //   });

  //   setS3Client(new AWS.S3());
  //   setCurrentPath(s3TokenResponse.allowed_prefix); // Start at the root folder
  // }, [s3TokenResponse]);

  // const _isInTheSameLevel = (key?: string, folderPath?: string): boolean => {

  //   if (!key || !folderPath) {
  //     return false;
  //   }

  //   const path: string = folderPath.endsWith("/") ? folderPath : `${folderPath}/`;
  //   const objectKey: string = key.endsWith("/") ? key : `${key}/`;

  //   // Check if the length of the key is exactly one more then the length of the path
  //   return objectKey.split("/").length - 1 === path.split("/").length;
  // }

  // const fetchS3BucketContents = useCallback(async (folderPath: string) => {
  //   if (!s3Client || !s3TokenResponse) return;

  //   try {
  //     const response = await s3Client
  //       .listObjectsV2({
  //         Bucket: s3TokenResponse.bucket,
  //         Prefix: `${folderPath}`,
  //       })
  //       .promise();

  //     if (response.Contents) {
  //       const formattedFiles = response.Contents
  //         .filter((obj) => obj.Key && obj.Key !== `${folderPath}/`)
  //         .filter((obj) => _isInTheSameLevel(obj.Key, folderPath))
  //         .map(
  //           (obj) =>
  //           ({
  //             id: obj.Key,
  //             name: obj.Key?.endsWith("/")
  //               ? obj.Key?.split("/").slice(-2, -1)[0] // Folder name
  //               : obj.Key?.split("/").pop(), // File name
  //             size: obj.Size,
  //             isDir: obj.Key?.endsWith("/") || false,
  //             openable: obj.Key?.endsWith("/") || false,
  //             dndOpenable: obj.Key?.endsWith("/") || false,
  //             color: theme.token.colorPrimary,
  //             thumbnailUrl: undefined,
  //           } as FileData)
  //         );

  //       setFiles(formattedFiles);
  //     }
  //   } catch (error) {
  //     console.error("Error fetching S3 objects:", error);
  //   }
  // }, [s3Client, s3TokenResponse, theme.token.colorPrimary]);

  // useEffect(() => {
  //   if (currentPath) {
  //     fetchS3BucketContents(currentPath);
  //   }
  // }, [currentPath, fetchS3BucketContents]);

  // const navigateTo = (folderPath: string) => {
  //   if (folderPath !== currentPath) {
  //     setPathHistory((prev) => [...prev, currentPath]); // Save history before changing
  //     setCurrentPath(folderPath);
  //   }
  // };

  // const goBack = () => {
  //   setPathHistory((prev) => {
  //     if (prev.length === 0) return prev;
  //     const previousPath = prev[prev.length - 1];
  //     setCurrentPath(previousPath);
  //     return prev.slice(0, -1); // Remove last path
  //   });
  // };

  // const refreshFiles = useCallback(() => {
  //   fetchS3BucketContents(currentPath);
  // }, [currentPath , fetchS3BucketContents] );



  // const uploadFileToS3 = async (file: File | UploadFile): Promise<void> => {

  //   if (!s3Client || !s3TokenResponse) {
  //     return;
  //   }

  //   // Concat the given key to the current path
  //   const objectKey: string = `${currentPath.endsWith("/") ? currentPath : `${currentPath}/`}${file.name}`

  //   try {
  //     const uploadParams = {
  //       Bucket: s3TokenResponse?.bucket,
  //       Key: objectKey,
  //       Body: file,
  //     };

  //     await s3Client.upload(uploadParams).promise();

  //     toast.success(`File ${file.name} uploaded successfully`);

  //   } catch (error) {
  //     console.error("Error uploading file to S3:", error);
  //     throw error;
  //   }
  // }

  // const deleteFileFromS3 = async (fileName: string): Promise<void> => {
  //   if (!s3Client || !s3TokenResponse) {
  //     return;
  //   }

  //   // Construct the full object key
  //   const objectKey: string = `${currentPath.endsWith("/") ? currentPath : `${currentPath}/`}${fileName}`;
  //   const bucket: string = s3TokenResponse.bucket;

  //   try {
  //     const deleteParams = {
  //       Bucket: bucket,
  //       Key: objectKey,
  //     };

  //     await s3Client.deleteObject(deleteParams).promise();

  //     toast.success(`File ${fileName} deleted successfully`);

    
  //   } catch (error) {
  //     toast.error(`Failed to delete file ${fileName}`);
  //     throw error;
  //   }
  // };


  // useEffect(() => {
  //   refreshFiles();
  // }, [currentPath , refreshFiles])

  return (
    <></>
    // <FileNavigContext.Provider value={{ files, currentPath, navigateTo, goBack, refreshFiles, uploadFileToS3 , deleteFileFromS3, inRootPath }}>
    //   {children}
    // </FileNavigContext.Provider>
  );
};

export const useFileNavigation = (): FileNavigContextType => {
  const context = useContext(FileNavigContext);
  if (!context) {
    throw new Error("useFileNavigation must be used within a FileNavigProvider");
  }
  return context;
};
