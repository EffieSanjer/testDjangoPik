import { extend } from 'vee-validate';

extend('phone', (value ) => {
  const tester = /^\+7\d{10}$/g;
  const isMatch = tester.test(value);

  if (isMatch) {
    return true
  }

  return 'Неверный формат (введите через +7)';
});

extend('email', (value) => {
  const tester = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/g;
  const isMatch = tester.test(value);

  if (isMatch) {
    return true
  }

  return 'Неверный формат';
});
