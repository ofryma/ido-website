import * as React from 'react';
import { motion } from "framer-motion";
import { Button, Typography } from 'antd';
import { useNavigate } from 'react-router-dom';

export interface IHeroSectionProps {
}

const { Title, Paragraph } = Typography;

export function HeroSection (props: IHeroSectionProps) {

    const navigate = useNavigate();

  return (
    <div>
      {/* Hero Section */}
      <motion.div initial={{ opacity: 0, y: 50 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8 }}>
          <Title style={{ fontSize: "32px", fontWeight: "bold" }}>Smart Storage for Photographers</Title>
          <Paragraph style={{ fontSize: "16px", maxWidth: "90%", margin: "auto" }}>
            Securely store, organize, and detect faces in your photos. Get notified when a face is recognized and easily share results with your clients.
          </Paragraph>
          <Button type="primary" size="large" style={{ marginTop: "20px" }} onClick={() => navigate("/signup")}>Get Started</Button>
        </motion.div>
    </div>
  );
}
