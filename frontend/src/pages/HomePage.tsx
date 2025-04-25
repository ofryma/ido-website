import { Layout, Typography, Row, Col, Card } from "antd";
import { StyledFooter } from "../components/design/Footer";
import { TopNavbar } from "../components/design/TopNavbar";
import { Content } from "antd/es/layout/layout";
import { motion } from "framer-motion";
import { SearchOutlined, TeamOutlined, SafetyOutlined } from '@ant-design/icons';

const { Title, Paragraph } = Typography;

const fadeInUp = {
  initial: { opacity: 0, y: 20 },
  animate: { opacity: 1, y: 0 },
  transition: { duration: 0.5 }
};

const HomePage = () => {
  
  
  return (
    <Layout style={{ minHeight: "100vh", direction: "rtl" }}>
      <TopNavbar />

      <Content style={{ display: "flex", flexDirection: "column", alignItems: "center", minHeight: "60vh", gap: "20px" }}>
        {/* Hero Section */}
        <div style={{ 
          width: "100%", 
          height: "80vh",
          position: "relative",
          overflow: "hidden"
        }}>
          <div style={{
            position: "absolute",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            backgroundImage: "url('/assets/images/cover_image.jpg')",
            backgroundSize: "cover",
            backgroundPosition: "center",
            zIndex: 0
          }} />
          <div style={{
            position: "absolute",
            top: 0,
            left: 0,
            right: 0,
            bottom: 0,
            background: "linear-gradient(135deg, rgba(0, 0, 0, 0.7) 0%, rgba(0, 0, 0, 0.5) 100%)",
            zIndex: 1
          }} />
          <Row justify="center" align="middle" style={{ 
            maxWidth: 1200, 
            margin: "0 auto", 
            position: "relative", 
            zIndex: 2,
            height: "100%",
            padding: "0 20px"
          }}>
            <Col xs={24} md={12}>
              <motion.div
                initial={{ opacity: 0, x: 50 }}
                animate={{ opacity: 1, x: 0 }}
                transition={{ duration: 0.5 }}
              >
                <Title level={1} style={{ 
                  color: "white", 
                  marginBottom: 24, 
                  textAlign: "right",
                  fontSize: "3.5rem",
                  textShadow: "2px 2px 4px rgba(0,0,0,0.3)"
                }}>
                  עידו מקדסי שמאות מקרקעין והערכת שווי
                </Title>
              </motion.div>
            </Col>
          </Row>
        </div>

        {/* About Section with Cards */}
        <div style={{ width: "100%", padding: "80px 20px", background: "#f5f5f5" }}>
          <Row justify="center" gutter={[24, 24]} style={{ maxWidth: 1200, margin: "0 auto" }}>
            <Col span={24} style={{ textAlign: "center", marginBottom: 48 }}>
              <motion.div {...fadeInUp}>
                <Title level={2}>אודותינו</Title>
              </motion.div>
            </Col>
            <Col xs={24} md={8} style={{ display: "flex", justifyContent: "center" }}>
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.2 }}
                style={{ width: "100%" }}
              >
                <Card 
                  hoverable 
                  style={{ 
                    height: "400px", 
                    width: "100%",
                    textAlign: "right",
                    display: "flex",
                    flexDirection: "column"
                  }}
                  bodyStyle={{ 
                    flex: 1,
                    display: "flex",
                    flexDirection: "column",
                    justifyContent: "space-between",
                    padding: "24px"
                  }}
                >
                  <div>
                    <TeamOutlined style={{ fontSize: 48, color: "#1890ff", marginBottom: 24 }} />
                    <Title level={4}>השכלה</Title>
                    <Paragraph>
                      בוגר תואר ראשון בהצטיינות בכלכלה וניהול במסלול האקדמי המכללה למנהל
                    </Paragraph>
                    <Paragraph>
                      בוגר תואר שני בהצטיינות בלימודי משפט באוניברסיטת בר אילן
                    </Paragraph>
                    <Paragraph>
                      שמאי מקרקעין
                    </Paragraph>
                  </div>
                </Card>
              </motion.div>
            </Col>
            <Col xs={24} md={8} style={{ display: "flex", justifyContent: "center" }}>
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.4 }}
                style={{ width: "100%" }}
              >
                <Card 
                  hoverable 
                  style={{ 
                    height: "400px", 
                    width: "100%",
                    textAlign: "right",
                    display: "flex",
                    flexDirection: "column"
                  }}
                  bodyStyle={{ 
                    flex: 1,
                    display: "flex",
                    flexDirection: "column",
                    justifyContent: "space-between",
                    padding: "24px"
                  }}
                >
                  <div>
                    <SafetyOutlined style={{ fontSize: 48, color: "#1890ff", marginBottom: 24 }} />
                    <Title level={4}>הסמכה מקצועית</Title>
                    <Paragraph>
                      עידו מקדסי שמאי מקרקעין מוסמך בהצטיינות
                    </Paragraph>
                  </div>
                </Card>
              </motion.div>
            </Col>
            <Col xs={24} md={8} style={{ display: "flex", justifyContent: "center" }}>
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.6 }}
                style={{ width: "100%" }}
              >
                <Card 
                  hoverable 
                  style={{ 
                    height: "400px", 
                    width: "100%",
                    textAlign: "right",
                    display: "flex",
                    flexDirection: "column"
                  }}
                  bodyStyle={{ 
                    flex: 1,
                    display: "flex",
                    flexDirection: "column",
                    justifyContent: "space-between",
                    padding: "24px"
                  }}
                >
                  <div>
                    <SearchOutlined style={{ fontSize: 48, color: "#1890ff", marginBottom: 24 }} />
                    <Title level={4}>תחומי התמחות</Title>
                    <Paragraph>
                      מתמחה בהערכת שווי, מיסוי מקרקעין והיטלי השבחה, חוות דעת לבתי משפט בדיקות טרום רכישה וייעוץ עסקי
                    </Paragraph>
                  </div>
                </Card>
              </motion.div>
            </Col>
          </Row>
        </div>

        {/* Profile Image Section */}
        <div style={{ width: "100%", padding: "40px 20px", background: "white" }}>
          <Row justify="center" style={{ maxWidth: 1200, margin: "0 auto" }}>
            <Col xs={24} md={16}>
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5 }}
              >
                <img 
                  src="/assets/images/profile_image.jpeg" 
                  alt="עידו מקדסי" 
                  style={{ 
                    width: "100%",
                    borderRadius: "8px",
                    boxShadow: "0 4px 12px rgba(0,0,0,0.15)"
                  }}
                />
              </motion.div>
            </Col>
          </Row>
        </div>

        {/* Logo Section */}
        <div style={{ width: "100%", padding: "20px", background: "white" }}>
          <Row justify="center" style={{ maxWidth: 1200, margin: "0 auto" }}>
            <Col xs={24} md={6}>
              <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ duration: 0.5, delay: 0.2 }}
                style={{ maxWidth: "200px", margin: "0 auto" }}
              >
                <img 
                  src="/assets/images/logo.jpeg" 
                  alt="Logo" 
                  style={{ 
                    width: "100%",
                    borderRadius: "8px",
                    boxShadow: "0 4px 12px rgba(0,0,0,0.15)"
                  }}
                />
              </motion.div>
            </Col>
          </Row>
        </div>

      </Content>

      <StyledFooter />
    </Layout>
  );
};

export default HomePage;
