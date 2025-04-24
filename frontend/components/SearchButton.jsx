import React from 'react';
import { SearchOutlined } from '@ant-design/icons';
import { Button } from 'antd';

const SearchButton = ({ onClick, disabled }) => (
  <Button
    onClick={onClick}
    disabled={disabled}
    type="primary"
    icon={<SearchOutlined />}
    style={{
      height: '40px',
      width: '100px'
    }}
  >
    Поиск
  </Button>
);

export default SearchButton;