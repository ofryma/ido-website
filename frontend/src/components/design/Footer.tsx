import { Layout, Typography, Row, Col, Space, theme } from 'antd';
import { useTheme } from '../../providers/theme/ThemeProvider';
import { useAppConfig } from '../../providers/app-config/AppConfigProvider';
import Icon, { FacebookOutlined, InstagramOutlined, TwitterOutlined, LinkedinOutlined, PhoneOutlined, MailOutlined, EnvironmentOutlined } from '@ant-design/icons';

export interface IFooterProps {}

const { Footer } = Layout;
const { Paragraph, Title } = Typography;

export function StyledFooter(props: IFooterProps) {
    const { theme } = useTheme();
    const { companyName } = useAppConfig();

    const contactInfo = {
        phone: "⁦+972 50-765-7334",
        email: "idomak22@gmail.com",
        address: "התבור 8, גן יבנה",
        services: [
            "הערכת שווי שוק",
            "שומות נגדיות להיטל השבחה",
            "חוות דעת לבתי משפט",
            "ייעוץ נדל״ן",
        ],
        socialMedia: [
            {
                icon: FacebookOutlined,
                name: "Facebook",
                url: "https://www.facebook.com/share/1BL9HmszEc/?mibextid=wwXIfr"
            },
            {
                icon: InstagramOutlined,
                name: "Instagram",
                url: "https://www.instagram.com/ido_mak?igsh=MWN2a2ZraTY0azFhZw=="
            },
            // {
            //     icon: TwitterOutlined,
            //     name: "Twitter",
            //     url: "https://twitter.com"  
            // },
            // {
            //     icon: LinkedinOutlined,
            //     name: "LinkedIn",
            //     url: "https://linkedin.com"
            // }
        ]
    }

    return (
        <div style={{ direction: 'rtl' }}>
            <Footer style={{ 
                textAlign: "center", 
                padding: "40px 20px",
                background: theme.token.colorBgBase,
                borderTop: `1px solid ${theme.token.colorBorder}`
            }}>
                <Row gutter={[32, 32]} justify="center">
                    <Col xs={24} md={8}>
                        <Title level={5} style={{ marginBottom: 16 }}>צור קשר</Title>
                        <Space direction="vertical" size="middle">
                            <Space>
                                <PhoneOutlined />
                                <Paragraph style={{ margin: 0 }}><a href={`tel:${contactInfo.phone}`}>{contactInfo.phone}</a></Paragraph>
                            </Space>
                            <Space>
                                <MailOutlined />
                                <Paragraph style={{ margin: 0 }}><a href={`mailto:${contactInfo.email}`}>{contactInfo.email}</a></Paragraph>
                            </Space>
                            <Space>
                                <EnvironmentOutlined />
                                <Paragraph style={{ margin: 0 }}>{contactInfo.address}</Paragraph>
                            </Space>
                        </Space>
                    </Col>
                    <Col xs={24} md={8}>
                        <Title level={5} style={{ marginBottom: 16 }}>שירותים</Title>
                        <Space direction="vertical" size="small">
                            {contactInfo.services.map((service, index) => (
                                <Paragraph key={index} style={{ margin: 0 }}>{service}</Paragraph>
                            ))}
                        </Space>
                    </Col>
                    <Col xs={24} md={8}>
                        <Title level={5} style={{ marginBottom: 16 }}>עקבו אחרינו</Title>
                        <Space size="large">
                            {contactInfo.socialMedia.map((media, index) => (
                                <a href={media.url} target="_blank" rel="noopener noreferrer">
                                    <Icon component={media.icon} style={{ fontSize: 24, color: theme.token.colorPrimary }} />
                                </a>
                            ))}
                        </Space>
                    </Col>
                </Row>
                <div style={{ marginTop: 32, borderTop: `1px solid ${theme.token.colorBorder}`, paddingTop: 20 }}>
                    {/* <Paragraph style={{ margin: 0, color: theme.token.colorTextBase }}>
                        &copy; 2025 {companyName}. כל הזכויות שמורות.
                    </Paragraph> */}
                </div>
            </Footer>
        </div>
    );
}
