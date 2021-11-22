import { Layout } from 'antd';
import PendingTransactions from './Pages/PendingTransactions';
import './App.css';

const { Header, Content, Footer } = Layout;

const App = () => (
    <Layout className="layout">
        <Header>
            <div className="logo" />
            <div className="headerTitle">VeriBlock MemPool</div>
        </Header>
        <Content style={{ padding: '0 50px' }}>
            <div className="site-layout-content">
                <PendingTransactions />
            </div>
        </Content>
        <Footer style={{ textAlign: 'center' }}>VeriBlock ©2021</Footer>
    </Layout>
);

export default App;
