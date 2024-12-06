<template>
    <div class="login">

        <el-form ref="loginRef" :model="loginForm" :rules="loginRules" class="login-form">
            <h3 class="title">大数据交通流量预测平台</h3>

            <el-form-item prop="username">

                <el-input v-model="loginForm.username" type="text" size="large" auto-complete="off" placeholder="账号">
                    <template #prefix><svg-icon icon="user" /></template>
                </el-input>
            </el-form-item>
            <el-form-item prop="password">
                <el-input v-model="loginForm.password" type="password" size="large" auto-complete="off"
                    placeholder="密码">
                    <template #prefix><svg-icon icon="password" /></template>
                </el-input>
            </el-form-item>


            <el-checkbox v-model="loginForm.rememberPassword" style="margin:0px 0px 25px 0px;">记住密码</el-checkbox>
            <el-form-item style="width:100%;">
                <el-button @click.prevent="handleLogin" size="large" type="primary" style="width:100%;">
                    <span>登 录</span>

                </el-button>

            </el-form-item>
        </el-form>
        <!--  底部  -->
        <div class="el-login-footer">
            <span>Copyright © 2024-2026 <a href="https://cixv20241115133921693.pingcode.com"
                    target="_blank">SDUST:智能交通团队</a>
                版权所有.</span>
        </div>
    </div>
</template>

<script setup>
    import { ref } from 'vue'
    import requestUtil from '@/utils/request'
    import qs from 'qs'
    import { ElMessage } from 'element-plus'
    import Cookies from "js-cookie";
    import { encrypt, decrypt } from "@/utils/jsencrypt";
    import router from '@/router'

    const loginForm = ref({
        username: '',
        password: '',
        rememberPassword: false,
    })

    const loginRules = {  //表单验证规则
        username: [{ required: true, message: '请输入账号', trigger: 'blur' }],
        password: [{ required: true, message: '请输入密码', trigger: 'blur' }],
    }

    const loginRef = ref(null)

    const handleLogin = () => {
        // validate使用async异步函数作为回调函数，回调函数可以获取到valid作为参数
        loginRef.value.validate(async (valid) => {
            if (valid) { //验证通过
                // ?后面的部分会以username=xxx&password=xxx的形式拼接到url后面，作为键值对的效果传给后端                   
                let result = await requestUtil.post('/user/login?' + qs.stringify(loginForm.value))  //登录请求
                console.log(result)
                console.log(result.data.user)
                let data = result.data
                if (data.code === 200) {
                    // 登录成功
                    ElMessage.success(data.message)
                    window.sessionStorage.setItem('token', data.token) //保存token到sessionStorage
                    window.sessionStorage.setItem('currentUser', JSON.stringify(data.user))  //保存用户信息到sessionStorage
                    window.sessionStorage.setItem("menuList", JSON.stringify(data.menuList))  //保存菜单列表到sessionStorage
                    // JSON.parse()方法可以将字符串转换为json对象(与JSON.stringify相反)
                    if (loginForm.value.rememberPassword) {
                        // 如果记住密码，则保存到cookie
                        Cookies.set("username", loginForm.value.username, { expires: 30 });  //保存用户名到cookie，有效期30天
                        Cookies.set("password", encrypt(loginForm.value.password), { expires: 30 });  //保存加密后的密码到cookie，有效期30天
                        Cookies.set("rememberPassword", loginForm.value.rememberMe, { expires: 30 });  //保存记住密码选项到cookie，有效期30天

                    }
                    else {
                        // 如果不记住密码，则删除cookie
                        Cookies.remove("username");
                        Cookies.remove("password");
                        Cookies.remove("rememberMe");
                    }
                    // 跳转到首页
                    router.push({ name: 'index' })
                }
                else {
                    // 登录失败,账号或密码错误
                    console.log(data.message)
                    ElMessage.error(data.message)
                }
            }
            else {//验证不通过
                console.log('验证失败')
            }
        })
    }

    function getCookie() {
        const username = Cookies.get("username");
        const password = Cookies.get("password");
        const rememberPassword = Cookies.get("rememberPassword");
        loginForm.value = {
            // 如果cookie中没有定义，则使用登陆表单中的默认值，否则使用cookie中的值
            username: username === undefined ? loginForm.value.username : username,
            password: password === undefined ? loginForm.value.password : decrypt(password),
            rememberPassword: rememberPassword === undefined ? false : Boolean(rememberPassword)
        };
    }
    getCookie();

</script>

<style lang="scss" scoped>
    a {
        color: white
    }

    .login {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
        background-image: url("../../assets/images/login-background.jpg");
        background-size: cover;
    }

    .title {
        font-size: 22px;
        margin: 0px auto 30px auto;
        text-align: center;
        color: #302f2f;
    }

    .login-form {
        border-radius: 6px;
        background: #ffffff;
        width: 400px;
        padding: 25px 25px 1px 25px;

        .el-input {
            height: 40px;



            input {
                display: inline-block;
                height: 40px;
            }
        }

        .input-icon {
            height: 39px;
            width: 14px;
            margin-left: 0px;
        }

    }

    .login-tip {
        font-size: 13px;
        text-align: center;
        color: #bfbfbf;
    }

    .login-code {
        width: 33%;
        height: 40px;
        float: right;

        img {
            cursor: pointer;
            vertical-align: middle;
        }
    }

    .el-login-footer {
        height: 40px;
        line-height: 40px;
        position: fixed;
        bottom: 0;
        width: 100%;
        text-align: center;
        color: #0f0f0f;
        font-family: Arial;
        font-size: 12px;
        letter-spacing: 1px;

        span {
            color: #0f0f0f;
            /* 将文本颜色设置为黑色 */
        }

        a {
            color: #0f0f0f;
            /* 设置链接文本颜色为黑色 */
            /* text-decoration: none; 如果需要，可以去掉下划线 */
        }
    }

    .login-code-img {
        height: 40px;
        padding-left: 12px;
    }
</style>