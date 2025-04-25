import { Button } from 'antd';
import { useNavigate } from 'react-router-dom';

export interface ISignupButtonProps {
}

export function SignupButton(props: ISignupButtonProps) {
    const navigate = useNavigate();

    return (
        <div>
            <Button type="default" onClick={() => navigate("/signup")}>Signup</Button>
        </div>
    );
}
