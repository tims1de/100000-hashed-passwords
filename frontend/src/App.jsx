import { useState } from 'react';
import SearchLine from "../components/search.jsx";
import SearchButton from "../components/SearchButton.jsx";
import axios from 'axios';

const App = () => {
  const [password, setPassword] = useState('');
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleSearch = () => {
    if (!password) return;

    setLoading(true);

    axios.get('http://127.0.0.1:8000/check_password', {
      params: {
        password: password
      }
    })
    .then((res) => {
      setResponse(res.data);
      setLoading(false);
    })
    .catch((error) => {
      console.error('Error:', error);
      setResponse({ error: "Ошибка при выполнении запроса" });
      setLoading(false);
    });
  };

  return (
    <div style={{
      display: 'flex',
      justifyContent: 'center',
      alignItems: 'center',
      minHeight: '100vh',
      padding: '20px',
      boxSizing: 'border-box'
    }}>
      <div style={{
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
        gap: '20px',
        width: '100%'
      }}>
        <div style={{ fontSize: 35, color: '#666' }}>
          Введите хэшированный пароль
        </div>

        <div style={{
          display: 'flex',
          gap: '10px',
          maxWidth: '800px',
          width: '100%',
          justifyContent: 'center'
        }}>
          <SearchLine
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSearch()}
          />
          <SearchButton
            onClick={handleSearch}
            disabled={loading}
          />
        </div>

        {loading && <div>Загрузка...</div>}

        {response && (
          <div style={{
            padding: '20px',
            backgroundColor: '#f5f5f5',
            borderRadius: '8px',
            maxWidth: '800px',
            width: '100%',
            textAlign: 'center'
          }}>
            {response.error ? (
              <div style={{ color: 'red' }}>{response.error}</div>
            ) : response.length === 0 ? (
              <div style={{ color: 'red' }}>Пароль не найден!</div>
            ) : (
              <div>Ваш пароль - {response[0]?.password}</div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;