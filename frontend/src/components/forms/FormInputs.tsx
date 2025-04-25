// frontend/src/components/forms/FormInputs.tsx
import React from 'react';
import { Input } from 'antd';
import { motion } from 'framer-motion';
import { useTheme } from '../../providers/theme/ThemeProvider';
import { inputWrapperVariants } from '../../styles/motionVariants';

interface FormInputsProps {
  name: string;
  setName: (value: string) => void;
  phone: string;
  setPhone: (value: string) => void;
}

export const FormInputs: React.FC<FormInputsProps> = ({ name, setName, phone, setPhone }) => {
  const { currentTheme } = useTheme();

  const inputStyle = {
    borderRadius: currentTheme.borderRadius.small,
    padding: '14px',
    border: `1px solid ${currentTheme.colors.border}`,
    background: currentTheme.colors.background,
    fontSize: currentTheme.typography.paragraph.fontSize,
    height: '48px',
    color: currentTheme.colors.text,
  };

  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      transition={{ delay: 0.2 }}
    >
      <motion.div
        variants={inputWrapperVariants}
        initial="rest"
        whileHover="focus"
        animate="rest"
        style={{ marginBottom: currentTheme.spacing.medium }}
      >
        <Input
          placeholder="Full Name"
          value={name}
          onChange={e => setName(e.target.value)}
          style={inputStyle}
        />
      </motion.div>
      <motion.div
        variants={inputWrapperVariants}
        initial="rest"
        whileHover="focus"
        animate="rest"
        style={{ marginBottom: currentTheme.spacing.xlarge }}
      >
        <Input
          placeholder="Phone Number"
          value={phone}
          onChange={e => setPhone(e.target.value)}
          style={inputStyle}
        />
      </motion.div>
    </motion.div>
  );
};