var Auth = {
	vars: {
		lowin: document.querySelector('.lowin'),
		lowin_brand: document.querySelector('.lowin-brand'),
		lowin_wrapper: document.querySelector('.lowin-wrapper'),
		lowin_login: document.querySelector('.lowin-login'),
		lowin_wrapper_height: 0,
		login_back_link: document.querySelector('.login-back-link'),
		forgot_link: document.querySelector('.forgot-link'),
		login_link: document.querySelector('.login-link'),
		login_btn: document.querySelector('.login-btn'),
		register_link: document.querySelector('.register-link'),
		register_btn:document.querySelector('#register'),
		password_group: document.querySelector('.password-group'),
		password_group_height: 0,
		lowin_register: document.querySelector('.lowin-register'),
		lowin_footer: document.querySelector('.lowin-footer'),
		box: document.getElementsByClassName('lowin-box'),
		name_input:document.querySelector("[name='registerName']"),
		email_input:document.querySelector("[name='registerEmail']"),
		password_input:document.querySelector("[name='registerPassword']"),
		name_erro:document.querySelector('#nameErro'),
		email_erro:document.querySelector('#emailErro'),
		password_erro:document.querySelector('#passwordErro'),
		name_flag:0,
		email_flag:0,
		password_flag:0,
		PUBLIC_KEY : 'MIIBITANBgkqhkiG9w0BAQEFAAOCAQ4AMIIBCQKCAQB+D6XE0YI03iyftOeE5bRe' +
            'dEKinVYiYbZmAEM833FoBIfY28ZT2a1Npnb5YTS7tw2bQTpvydZwq229r53y2/jO' +
            '/VdtCjCsMtNnpSAhahCbdrbMSPkLvLrkHsZh55hX+drId74HU4oaMtk9DROdOWd2' +
            'MzBhxaA97Z3uSB1ICX4P1Xmeif2cCgUFefMFPOiWn8OgpeI+vkne5xpbGP5HT5y7' +
            'JtRsg5H9wn87MvwaRyQNH7ep7Lvt555ZBtUiKDRX5MgMmg1eVgvayibFLP7fOHHS' +
            'e+5yjnf08wsNsd/vltiCAeRhUzFe4Ux8NWz4XX3Nn6zUj8jx5wSswDnzDbv27lcJ' +
            'AgMBAAE=',
	},
	register(e) {
		Auth.vars.lowin_login.className += ' lowin-animated';
		setTimeout(() => {
			Auth.vars.lowin_login.style.display = 'none';
		}, 500);
		Auth.vars.lowin_register.style.display = 'block';
		Auth.vars.lowin_register.className += ' lowin-animated-flip';
		Auth.setHeight(Auth.vars.lowin_register.offsetHeight + Auth.vars.lowin_footer.offsetHeight);

		e.preventDefault();
	},
	registerAction(e){
		var c="{'name':'"+$(Auth.vars.name_input).val()+
			"','email':'"+$(Auth.vars.email_input).val()+
			"','password':'"+$(Auth.vars.password_input).val()+"'}"

		var encrypt = new JSEncrypt();
		  //encrypt.setPrivateKey('-----BEGIN RSA PRIVATE KEY-----'+PRIVATE_KEY+'-----END RSA PRIVATE KEY-----');
        encrypt.setPublicKey('-----BEGIN PUBLIC KEY-----' + Auth.vars.PUBLIC_KEY + '-----END PUBLIC KEY-----');
        var m = encrypt.encrypt(c);
        $.ajax({
        url: 'firstRegister/',
        type:'post',
        dataType:'json',
        traditional:true,//这个参数必须添加，采用传统方式转换
        data : {raw:m},
        success:function (result) {
            if(result.resultCode == 0) {
                alert("成功")
            }else{
                alert("失败")
            }
        }
    });
		e.preventDefault();
	},
	registerCheck(e){
		e.preventDefault();
		if(Auth.vars.name_flag*Auth.vars.email_flag*Auth.vars.password_flag==1)
			return true
		return  false
	},
	login(e) {
		Auth.vars.lowin_register.classList.remove('lowin-animated-flip');
		Auth.vars.lowin_register.className += ' lowin-animated-flipback';
		Auth.vars.lowin_login.style.display = 'block';
		Auth.vars.lowin_login.classList.remove('lowin-animated');
		Auth.vars.lowin_login.className += ' lowin-animatedback';
		setTimeout(() => {
			Auth.vars.lowin_register.style.display = 'none';
		}, 500);
		
		setTimeout(() => {
			Auth.vars.lowin_register.classList.remove('lowin-animated-flipback');
			Auth.vars.lowin_login.classList.remove('lowin-animatedback');
		},1000);

		Auth.setHeight(Auth.vars.lowin_login.offsetHeight + Auth.vars.lowin_footer.offsetHeight);

		e.preventDefault();
	},
	forgot(e) {
		Auth.vars.password_group.classList += ' lowin-animated';

		setTimeout(() => {
			Auth.vars.login_back_link.style.opacity = 1;
			Auth.vars.password_group.style.height = 0;
			Auth.vars.password_group.style.margin = 0;
		}, 100);

		setTimeout(() => {
			Auth.vars.password_group.style.display = 'none';
			Auth.vars.login_back_link.style.display = 'block';
		}, 1000);
		Auth.vars.login_btn.innerText = '忘记密码';
		Auth.setHeight(Auth.vars.lowin_wrapper_height - Auth.vars.password_group_height);
		Auth.vars.lowin_login.querySelector('form').setAttribute('action', Auth.vars.option.forgot_url);

		e.preventDefault();
	},
	loginback(e) {
		Auth.vars.password_group.classList.remove('lowin-animated');
		Auth.vars.password_group.classList += ' lowin-animated-back';
		Auth.vars.password_group.style.display = 'block';

		setTimeout(() => {
			Auth.vars.login_back_link.style.opacity = 0;
			Auth.vars.password_group.style.height = Auth.vars.password_group_height + 'px';
			Auth.vars.password_group.style.marginBottom = 30 + 'px';
		}, 100);

		setTimeout(() => {
			Auth.vars.login_back_link.style.display = 'none';
			Auth.vars.password_group.classList.remove('lowin-animated-back');
		}, 1000);

		Auth.vars.login_btn.innerText = '登录';
		Auth.vars.lowin_login.querySelector('form').setAttribute('action', Auth.vars.option.login_url);

		Auth.setHeight(Auth.vars.lowin_wrapper_height);
		
		e.preventDefault();
	},
	setHeight(height) {
		Auth.vars.lowin_wrapper.style.minHeight = height + 'px';
	},
	brand() {
		Auth.vars.lowin_brand.classList += ' lowin-animated';
		setTimeout(() => {
			Auth.vars.lowin_brand.classList.remove('lowin-animated');
		}, 1000);
	},
	nullCheck(textObj,inputObj){
		var f=true
		if($(inputObj).val()==null || $(inputObj).val()=="") {
			$(textObj).find("label").text("不能为空哦").css("color","lightpink")
			$(textObj).slideDown("normal")
			f=false
		}
		return f;
	},
	inputClear(textObj){
		$(textObj).slideUp("normal")
	},
	nameCheck(textObj,inputObj){
		var f=true
		//检查用户名
		return f;
	},
	emailCheck(textObj,inputObj){
		var f=false
		var reg = new RegExp("^[a-z0-9]+([._\\-]*[a-z0-9])*@([a-z0-9]+[-a-z0-9]*[a-z0-9]+.){1,63}[a-z0-9]+$"); //正则表达式
		if (reg.test($(inputObj).val())){
			$(textObj).find("label").text("邮箱可以使用").css("color","lightgreen");
			f=true
		}
		else {
			$(textObj).find("label").text("格式不正确").css("color","lightpink");
		}
		$(textObj).slideDown("normal")
		return f;
	},
	passwordCheck(textObj,inputObj){
		var f=false
		var reg=/^([a-zA-Z0-9]){6,18}$/;
		if (reg.test($(inputObj).val())){
			$(textObj).find("label").text("密码可以").css("color","lightgreen");
			f=true
		}
		else {
			$(textObj).find("label").text("密码长度为6到18位字母和数字").css("color","lightpink");
		}
		$(textObj).slideDown("normal")
		return f;
	},
	init(option) {
		Auth.setHeight(Auth.vars.box[0].offsetHeight + Auth.vars.lowin_footer.offsetHeight);

		Auth.vars.password_group.style.height = Auth.vars.password_group.offsetHeight + 'px';
		Auth.vars.password_group_height = Auth.vars.password_group.offsetHeight;
		Auth.vars.lowin_wrapper_height = Auth.vars.lowin_wrapper.offsetHeight;

		Auth.vars.option = option;
		Auth.vars.lowin_login.querySelector('form').setAttribute('action', option.login_url);

		var len = Auth.vars.box.length - 1;

		for(var i = 0; i <= len; i++) {
			if(i !== 0) {
				Auth.vars.box[i].className += ' lowin-flip';
			}
		}

		Auth.vars.forgot_link.addEventListener("click", (e) => {
			Auth.forgot(e);
		});

		Auth.vars.register_link.addEventListener("click", (e) => {
			Auth.brand();
			Auth.register(e);
		});

		Auth.vars.login_link.addEventListener("click", (e) => {
			Auth.brand();
			Auth.login(e);
		});

		Auth.vars.login_back_link.addEventListener("click", (e) => {
			Auth.loginback(e);
		});

		Auth.vars.register_btn.addEventListener("click", (e) => {
			if (Auth.registerCheck(e)) {
				Auth.registerAction(e);
				Auth.brand();
				Auth.login(e);
			}
			return false;
		});

		Auth.vars.name_input.addEventListener("focus", (e) => {
			Auth.inputClear(Auth.vars.name_erro)
		});
		Auth.vars.name_input.addEventListener("blur", (e) => {
			if (Auth.nameCheck(Auth.vars.name_erro,Auth.vars.name_input)&&Auth.nullCheck(Auth.vars.name_erro,Auth.vars.name_input))
				Auth.vars.name_flag=1;
			else
				Auth.vars.name_flag=0;

		});

		Auth.vars.email_input.addEventListener("focus", (e) => {
			Auth.inputClear(Auth.vars.email_erro)
		});
		Auth.vars.email_input.addEventListener("blur", (e) => {
			if (Auth.emailCheck(Auth.vars.email_erro,Auth.vars.email_input)&&Auth.nullCheck(Auth.vars.email_erro,Auth.vars.email_input))
				Auth.vars.email_flag=1;
			else
				Auth.vars.email_flag=0;
		});

		Auth.vars.password_input.addEventListener("focus", (e) => {
			Auth.inputClear(Auth.vars.password_erro)
		});
		Auth.vars.password_input.addEventListener("blur", (e) => {
			if(Auth.passwordCheck(Auth.vars.password_erro,Auth.vars.password_input)&&Auth.nullCheck(Auth.vars.password_erro,Auth.vars.password_input))
				Auth.vars.password_flag=1;
			else
				Auth.vars.password_flag=0;

		});
	}
}