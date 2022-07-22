import React, { useState } from 'react';
import '../css/login.css';
import LoginForm from './LoginForm';

function Login() {
  const userTest = {
    email: 'user@user.com',
    password: 'user',
  };
  // test user hardcode details

  const [user, setUser] = useState({ name: '', email: '' });
  const [error, setError] = useState('');

  const Login = (details) => {
    console.log(details);

    if (
      details.email === userTest.email &&
      details.password === userTest.password
    )
      console.log('logged in');
  };

  const Logout = () => {
    console.log('logout');
  };

  return (
    <div className="App">
      {user.email !== '' ? (
        <div className="welcome">
          <h2>
            welcome, <span>{user.name}</span>
          </h2>
          <button>Logout</button>
        </div>
      ) : (
        <LoginForm Login={Login} error={error} />
      )}
    </div>
  );
}

export default Login;