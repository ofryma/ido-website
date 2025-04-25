// frontend/src/components/buttons/SubmitButton.tsx
import React from 'react';
import { Button } from 'antd';
import { motion } from 'framer-motion';
import { useTheme } from '../../providers/theme/ThemeProvider';
import { buttonVariants } from '../../styles/motionVariants';

interface SubmitButtonProps {
  onClick: () => void;
  label: string;
}

export const SubmitButton: React.FC<SubmitButtonProps> = ({ onClick, label }) => {
  const { currentTheme } = useTheme();

  return (
    <motion.div variants={buttonVariants} whileHover="hover" whileTap="tap">
      <Button
        onClick={onClick}
        block
        size="large"
        style={{
          height: '56px',
          borderRadius: currentTheme.borderRadius.medium,
          background: currentTheme.colors.buttonGradient,
          border: 'none',
          color: currentTheme.colors.card,
          fontSize: currentTheme.typography.paragraph.fontSize,
          fontWeight: 600,
          letterSpacing: '0.5px',
          boxShadow: currentTheme.shadows.button,
        }}
      >
        {label}
      </Button>
    </motion.div>
  );
};