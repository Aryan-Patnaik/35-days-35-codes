from cryptography import x509  # Importing x509 module from cryptography library for handling certificates
from cryptography.x509.oid import NameOID  # Importing NameOID for specifying X.509 attribute names
from cryptography.hazmat.primitives import hashes, serialization  # Importing hashes and serialization modules
from cryptography.hazmat.primitives.asymmetric import rsa  # Importing RSA for key generation
from cryptography.hazmat.backends import default_backend  # Importing default_backend for backend selection
from datetime import datetime, timedelta  # Importing datetime and timedelta for date calculations

def generate_key_pair():
    """Generate an RSA key pair with specified parameters."""
    key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    return key

def generate_certificate(subject_name, issuer_name, issuer_key, is_ca, key, serial_number):
    """Generate an X.509 certificate with specified parameters."""
    # Constructing subject name attributes
    subject = x509.Name([
        x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
        x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
        x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
        x509.NameAttribute(NameOID.ORGANIZATION_NAME, subject_name),
        x509.NameAttribute(NameOID.COMMON_NAME, subject_name),
    ])
    
    # Constructing issuer name attributes based on whether it's a CA certificate
    if not is_ca:
        issuer = x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"California"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, issuer_name),
            x509.NameAttribute(NameOID.COMMON_NAME, issuer_name),
        ])
    else:
        issuer = subject  # If it's a CA certificate, issuer is the same as subject
    
    # Building the certificate
    builder = x509.CertificateBuilder().subject_name(subject).issuer_name(issuer).public_key(
        key.public_key()).serial_number(serial_number).not_valid_before(
        datetime.utcnow()).not_valid_after(
        datetime.utcnow() + timedelta(days=365)
    )
    
    # Adding Basic Constraints extension for CA certificates
    if is_ca:
        builder = builder.add_extension(
            x509.BasicConstraints(ca=True, path_length=None), critical=True,
        )

    # Signing the certificate with the issuer's private key
    certificate = builder.sign(
        private_key=issuer_key, algorithm=hashes.SHA256(), backend=default_backend()
    )
    return certificate

# Generating the root CA key pair and certificate
root_key = generate_key_pair()
root_cert = generate_certificate("Root CA", "Root CA", root_key, True, root_key, 1)

# Saving Root CA key to file
with open("root_key.pem", "wb") as f:
    f.write(root_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))

# Saving Root CA certificate to file
with open("root_cert.pem", "wb") as f:
    f.write(root_cert.public_bytes(serialization.Encoding.PEM))

# Generating the server key pair and certificate signed by the root CA
server_key = generate_key_pair()
server_cert = generate_certificate("Server", "Root CA", root_key, False, server_key, 1000)

# Saving server key to file
with open("server_key.pem", "wb") as f:
    f.write(server_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    ))

# Saving server certificate to file
with open("server_cert.pem", "wb") as f:
    f.write(server_cert.public_bytes(serialization.Encoding.PEM))

print("Root CA and server certificates generated successfully!")  # Print confirmation message
