class RBAC:
    def __init__(self):
        # Initialize dictionaries to store users, roles, and permissions
        self.users = {}
        self.roles = {}
        self.permissions = {}

    def add_user(self, username):
        # Add a new user to the RBAC system
        if username not in self.users:
            self.users[username] = []
        else:
            print(f"User {username} already exists.")

    def add_role(self, role_name, permissions):
        # Add a new role to the RBAC system with associated permissions
        if role_name not in self.roles:
            self.roles[role_name] = permissions
        else:
            print(f"Role {role_name} already exists.")

    def assign_role_to_user(self, username, role_name):
        # Assign a role to a user
        if username in self.users:
            if role_name in self.roles:
                self.users[username].append(role_name)
            else:
                print(f"Role {role_name} does not exist.")
        else:
            print(f"User {username} does not exist.")

    def add_permission(self, permission_name):
        # Add a new permission to the RBAC system
        if permission_name not in self.permissions:
            self.permissions[permission_name] = []
        else:
            print(f"Permission {permission_name} already exists.")

    def assign_permission_to_role(self, role_name, permission_name):
        # Assign a permission to a role
        if role_name in self.roles:
            if permission_name not in self.permissions:
                self.permissions[permission_name] = []
            self.permissions[permission_name].append(role_name)
        else:
            print(f"Role {role_name} does not exist.")

    def check_permission(self, username, permission_name):
        # Check if a user has a specific permission
        if username in self.users:
            for role in self.users[username]:
                if role in self.permissions.get(permission_name, []):
                    return True
        return False

# Create an instance of the RBAC class
rbac = RBAC()

# Add users
rbac.add_user('alice')
rbac.add_user('bob')

# Add roles with associated permissions
rbac.add_role('admin', ['read', 'write', 'delete'])
rbac.add_role('editor', ['read', 'write'])
rbac.add_role('viewer', ['read'])

# Assign roles to users
rbac.assign_role_to_user('alice', 'admin')
rbac.assign_role_to_user('bob', 'editor')

# Add permissions
rbac.add_permission('read')
rbac.add_permission('write')
rbac.add_permission('delete')

# Assign permissions to roles
rbac.assign_permission_to_role('admin', 'read')
rbac.assign_permission_to_role('admin', 'write')
rbac.assign_permission_to_role('admin', 'delete')

rbac.assign_permission_to_role('editor', 'read')
rbac.assign_permission_to_role('editor', 'write')

rbac.assign_permission_to_role('viewer', 'read')

# Check permissions for users
print(f"Alice has read permission: {rbac.check_permission('alice', 'read')}")
print(f"Alice has delete permission: {rbac.check_permission('alice', 'delete')}")
print(f"Bob has write permission: {rbac.check_permission('bob', 'write')}")
print(f"Bob has delete permission: {rbac.check_permission('bob', 'delete')}")
