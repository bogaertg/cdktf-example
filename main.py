from cdktf import App, TerraformStack
from cdktf_cdktf_provider_tls.private_key import PrivateKey
from cdktf_cdktf_provider_random.password import Password
app = App()
stack = TerraformStack(app, "my_stack")
PrivateKey(stack, "my_key",
                 algorithm="RSA",
                 rsa_bits=2048)
Password(stack, "my_password",
                   length=16,
                   special=True)    

app.synth()

