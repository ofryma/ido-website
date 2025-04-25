// frontend/src/styles/motionVariants.ts
export const cardVariants = {
    hidden: { opacity: 0, y: 20 },
    visible: { 
      opacity: 1, 
      y: 0,
      transition: { 
        duration: 0.6, 
        ease: [0.25, 0.1, 0.25, 1] 
      }
    }
  };
  
  export const inputWrapperVariants = {
    focus: {
      boxShadow: '0 0 0 2px rgba(28, 100, 242, 0.2)',
      borderColor: '#1c64f2',
      transition: { duration: 0.2 }
    },
    rest: {
      boxShadow: 'none',
      borderColor: '#e2e8f0',
      transition: { duration: 0.2 }
    }
  };
  
  export const buttonVariants = {
    hover: { scale: 1.02 },
    tap: { scale: 0.98 }
  };
  
  export const captureVariants = {
    hover: { scale: 1.01 },
    tap: { scale: 0.95 }
  };
  
  export const imageVariants = {
    hidden: { opacity: 0 },
    visible: { opacity: 1 }
  };