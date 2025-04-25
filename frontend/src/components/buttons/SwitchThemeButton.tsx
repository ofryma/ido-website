import * as React from 'react';
import { Button } from 'antd';
import { SunOutlined, MoonOutlined } from '@ant-design/icons';
import { motion, AnimatePresence } from 'framer-motion';
import { useTheme } from '../../providers/theme/ThemeProvider';

export interface ISwitchThemeButtonProps { }

export function SwitchThemeButton(props: ISwitchThemeButtonProps) {

    const { themeMode, changeThemeMode } = useTheme();

    const handleChangeTheme = () => {
        changeThemeMode()
    }

    return (
        <Button
            type="primary"
            shape="circle"
            onClick={handleChangeTheme}
            style={{
                position: "fixed",
                bottom: 20,
                left: 20,
                zIndex: 1000,
                width: 50,
                height: 50,
                display: "flex",
                alignItems: "center",
                justifyContent: "center",
                overflow: "hidden",
            }}
        >
            <AnimatePresence mode="wait">
                <motion.div
                    key={themeMode === "dark" ? "moon" : "sun"}
                    initial={{ opacity: 0, scale: 0.5 }}
                    animate={{ opacity: 1, scale: 1, rotate: 360 }}
                    exit={{ opacity: 0, scale: 0.5 }}
                    transition={{ duration: 0.4, ease: "easeInOut" }}
                    style={{ position: "absolute" }}
                >
                    {themeMode === "dark" ? <MoonOutlined /> : <SunOutlined />}
                </motion.div>
            </AnimatePresence>
        </Button>
    );
}
