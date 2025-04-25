import * as React from 'react';
import { Button } from 'antd';
import { UserOutlined } from "@ant-design/icons";
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../../providers/auth/AuthProvider';

export interface IUserAvatarProps {
}


export function UserAvatar(props: IUserAvatarProps) {

    const navigate = useNavigate();
    const auth = useAuth();

    const handleLoginPress = () => {
        if (auth.isValid) {
            navigate("/photographer");
        } else {
            navigate("/login");
        }
    }

    return (
        <div>
            <Button shape="circle" icon={<UserOutlined />} onClick={handleLoginPress} />
        </div>
    );
}
