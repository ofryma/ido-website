// frontend/src/components/layout/StyledCard.tsx
import React from 'react';
import { motion } from 'framer-motion';
import { useTheme } from '../../providers/theme/ThemeProvider';
import { cardVariants } from '../../styles/motionVariants';
import { lightTheme, darkTheme } from '../../styles/theme';

interface StyledCardProps {
  children: React.ReactNode;
}

export const StyledCard: React.FC<StyledCardProps> = ({ children }) => {
  const { themeMode } = useTheme();
  const currentCustomTheme = themeMode === "light" ? lightTheme : darkTheme;

  return (
    <div style={{
      minHeight: '100vh',
      background: currentCustomTheme.colors.gradient,
      display: 'flex',
      alignItems: 'center',
      justifyContent: 'center',
      padding: '20px',
    }}>
      <motion.div
        variants={cardVariants}
        initial="hidden"
        animate="visible"
        style={{
          maxWidth: '500px',
          width: '100%',
          background: currentCustomTheme.colors.card,
          borderRadius: currentCustomTheme.borderRadius.large,
          padding: currentCustomTheme.spacing.xxlarge,
          boxShadow: currentCustomTheme.shadows.card,
          border: `1px solid ${currentCustomTheme.colors.border}`,
        }}
      >
        {children}
      </motion.div>
    </div>
  );
};