import React, { useState } from 'react';

function LoginForm({ Login, error }) {
  const [details, setDetails] = useState({ name: '', email: '', password: '' }); // sets default state of form

  const submitHandler = (e) => {
    e.preventDefault();
    Login(details); // prop with details passed through
  };
  //handles submit

  return (
    <form onSubmit={submitHandler}>
      {/* calls above function */}
      <div className="form-inner">
        <h2>Login</h2>
        {/* {ERROR} */}
        <div className="form-group">
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            name="name"
            id="name"
            onChange={(e) => setDetails({ ...details, name: e.target.value })}
            value={details.name}
          />
        </div>
        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input
            type="email"
            name="email"
            id="email"
            onChange={(e) => setDetails({ ...details, email: e.target.value })}
            value={details.email}
          />
        </div>
        <div className="form-group">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            name="password"
            id="password"
            onChange={(e) =>
              setDetails({ ...details, password: e.target.value })
            }
            value={details.password}
          />
        </div>
        <input type="submit" value="LOGIN" />
      </div>
    </form>

    // form
  );
}

export default LoginForm;
