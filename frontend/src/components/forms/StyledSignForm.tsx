import { Layout, Card, Typography, Spin } from "antd";
import { motion } from "framer-motion";

const { Content } = Layout;
const { Title, Paragraph } = Typography;

export interface IStyledSignFormProps {
    title: string;
    desc?: string;
    loading?: boolean;
    children?: any;
}

export function StyledSignForm (props: IStyledSignFormProps) {
  return (
    <>
        <Content style={{ display: "flex", justifyContent: "center", alignItems: "center", padding: "50px 16px" }}>
        <motion.div initial={{ opacity: 0, y: 50 }} animate={{ opacity: 1, y: 0 }} transition={{ duration: 0.8 }}>
            <Card style={{ width: 400, padding: "30px", textAlign: "center", borderRadius: "12px", boxShadow: "0 4px 10px rgba(0,0,0,0.1)" }}>
            
            {
                props.loading 
                ? <Spin/>
                : <Title level={3} style={{ marginBottom: "10px" }}>{props.title}</Title>
            }

            
            {
                props.desc &&
                <Paragraph style={{ color: "#666", marginBottom: "20px" }}>{props.desc}</Paragraph>
            }

            {props.children}

            </Card>
        </motion.div>
        </Content>
    </>
  );
}
