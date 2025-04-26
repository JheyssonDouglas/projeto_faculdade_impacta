<template>
  <div class="home">
    <img src="@/assets/Impacta.png" alt="Impacta Logo" />
    <h1>Bem-vindo à Impacta Food</h1>

    <div class="auth-container">
      <div v-if="isLogin">
        <h2>Login</h2>
        <input v-model="loginData.email" type="email" placeholder="Email" />
        <input v-model="loginData.password" type="password" placeholder="Senha" />
        <button @click="login">Entrar</button>
        <p>Não tem conta? <span @click="toggleAuth">Cadastre-se</span></p>
      </div>
      
      <div v-else>
        <h2>Cadastro</h2>
        <input v-model="registerData.nome" type="text" placeholder="Nome" />
        <input v-model="registerData.email" type="email" placeholder="Email" />
        <input v-model="registerData.password" type="password" placeholder="Senha" />
        <button @click="register">Cadastrar</button>
        <p>Já tem conta? <span @click="toggleAuth">Faça login</span></p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'HomePage',
  data() {
    return {
      isLogin: true,
      loginData: {
        email: '',
        password: ''
      },
      registerData: {
        nome: '',
        email: '',
        password: ''
      },
      showCartChoiceModal: false,
      lastCart: [],
    };
  },
  methods: {
    toggleAuth() {
      this.isLogin = !this.isLogin;
    },
    checkPreviousCart() {
    axios.get('/cart/')
      .then(res => {
        if (res.data && res.data.length > 0) {
          this.lastCart = res.data;
          this.showCartChoiceModal = true;
        }
      });
  },
  continueLastCart() {
    localStorage.setItem('cart', JSON.stringify(this.lastCart));
    this.$router.push('/produtos');
  },
    async login() {
      try {
        const response = await axios.post('http://localhost:8000/api/login/', this.loginData);
        if (response.data.success) {
          this.$router.push('/products');
        } else {
          alert('Email ou senha incorretos.');
        }
      } catch (error) {
        alert('Erro ao fazer login. Tente novamente.');
      }
    },
    async register() {
      try {
        const response = await axios.post('http://localhost:8000/api/register/', this.registerData);
        if (response.data.success) {
          alert('Cadastro realizado com sucesso! Faça login.');
          this.isLogin = true;
        } else {
          alert('Erro ao cadastrar. Verifique os dados.');
        }
      } catch (error) {
        alert('Erro ao cadastrar. Tente novamente.');
      }
    }
  }
};
</script>

<style scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  text-align: center;
}

img {
  margin-top: -100px;
  width: 300px;
}

.auth-container {
  margin-top: 20px;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 10px;
  width: 300px;
}

input {
  display: block;
  width: 100%;
  margin: 10px 0;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  width: 100%;
  padding: 10px;
  margin-top: 10px;
  cursor: pointer;
}

span {
  color: blue;
  cursor: pointer;
  text-decoration: underline;
}
</style>