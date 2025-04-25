import { Card, Typography } from 'antd';
import { motion } from 'framer-motion';
import * as React from 'react';
import { useTheme } from '../../providers/theme/ThemeProvider';

interface FeatureInfo {
    icon: React.ReactNode;
    title: string;
    desc: string;
}

export interface IFeatureCardProps {
    index: number;
    feature: FeatureInfo;
}

export function FeatureCard(props: IFeatureCardProps) {

    const { theme } = useTheme();

    return (
        <motion.div
            initial={{ opacity: 0, y: 30 }}
            whileInView={{ opacity: 1, y: 0 }}
            viewport={{ once: true }}
            transition={{ duration: 0.6, delay: props.index * 0.2 }}
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.98 }}
        >
            <Card
                hoverable
                style={{
                    textAlign: "center",
                    borderRadius: "14px",
                    boxShadow: "0 6px 14px rgba(0, 0, 0, 0.15)",
                    transition: "all 0.3s ease",
                    background: theme.token.colorTextBase,
                    border: "1px solid rgba(0,0,0,0.1)",
                    overflow: "hidden",
                }}
                cover={
                    <motion.div
                        style={{ fontSize: "50px", padding: "20px", color: theme.token.colorBgBase }}
                        initial={{ scale: 0.8, opacity: 0 }}
                        animate={{ scale: 1, opacity: 1 }}
                        transition={{ duration: 0.4, delay: props.index * 0.15 }}
                    >
                        {props.feature.icon}
                    </motion.div>
                }
            >
                <Typography.Title level={4} style={{ marginBottom: 8, color: theme.token.colorBgBase }}>
                    {props.feature.title}
                </Typography.Title>
                <Typography.Paragraph style={{ color: theme.token.colorBgBase, fontSize: "14px" }}>
                    {props.feature.desc}
                </Typography.Paragraph>
            </Card>
        </motion.div>
    );
}
