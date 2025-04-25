// frontend/src/utils/videoUtils.ts
import { RefObject } from 'react';
import { message } from 'antd';

export const startVideoStream = async (
  videoRef: RefObject<HTMLVideoElement | null>,
  streamRef: React.MutableRefObject<MediaStream | null>
) => {
  if (streamRef.current) {
    streamRef.current.getTracks().forEach(track => track.stop());
    streamRef.current = null;
    console.log("Previous stream stopped");
  }

  try {
    const stream = await navigator.mediaDevices.getUserMedia({ video: true });
    streamRef.current = stream;
    if (videoRef.current) {
      videoRef.current.srcObject = stream;
      videoRef.current.onloadedmetadata = () => {
        videoRef.current?.play().then(() => {
          console.log("Video stream started successfully");
        }).catch(err => {
          console.error("Error playing video:", err);
          message.error("Failed to start camera. Please allow camera access.");
        });
      };
    } else {
      console.error("Video element is not available");
      message.error("Camera element not found.");
    }
  } catch (err) {
    console.error("Error accessing camera:", err);
    message.error("Camera access denied or unavailable.");
  }
};

export const dataURLToBlob = async (dataURL: string) => {
  const response = await fetch(dataURL);
  return await response.blob();
};