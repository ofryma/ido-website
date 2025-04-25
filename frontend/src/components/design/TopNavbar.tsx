import * as React from 'react';

import { Layout, Typography } from 'antd';
import { motion } from 'framer-motion';
import { useTheme } from '../../providers/theme/ThemeProvider';
import { useNavigate } from 'react-router-dom';

export interface ITopNavbarProps {
    navigateHomeOnTitlePress?: boolean; 
    children?: any;
}

const { Header } = Layout;
const { Title } = Typography;

export function TopNavbar(props: ITopNavbarProps) {
    const { theme } = useTheme();
    const navigate = useNavigate();

    const handleNavigateHome = () => {
        if (props.navigateHomeOnTitlePress){
            navigate("/");
        }
    }

    return (
        <div style={{ direction: 'rtl' }}>
            <motion.div initial={{ opacity: 0, y: -20 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.6 }}>
                <Header onClick={handleNavigateHome} style={{ 
                    display: "flex", 
                    justifyContent: "space-between", 
                    alignItems: "center", 
                    padding: "0 16px",
                    backgroundColor: theme.token.colorHeaderBg,
                    direction: 'rtl'
                }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '12px' }}>
                        <img 
                            src="/assets/images/logo.jpeg" 
                            alt="Logo" 
                            style={{ 
                                height: '40px', 
                                width: 'auto',
                                borderRadius: '4px'
                            }} 
                        />
                        <Title level={2} style={{ 
                            margin: 0, 
                            fontSize: "20px",
                            color: theme.token.colorHeaderText,
                            textAlign: 'right'
                        }}>
                            עידו מקדסי - שמאות מקרקעין
                        </Title>
                    </div>
                    {props.children}
                </Header>
            </motion.div>
        </div>
    );
}
