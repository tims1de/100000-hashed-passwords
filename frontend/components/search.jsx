import { Input } from 'antd';

const SearchLine = ({ value, onChange, onKeyPress }) => (
  <Input
    type="text"
    placeholder="Введите параметры"
    value={value}
    onChange={onChange}
    onKeyPress={onKeyPress}
    style={{
      width: '500px',
      height: '40px',
      maxWidth: '100%'
    }}
  />
);

export default SearchLine;