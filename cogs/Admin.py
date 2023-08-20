import nextcord
from nextcord.ext import commands
from nextcord.ext.commands import has_permissions
from nextcord.utils import get

class Admin(commands.Cog):

    def __init__(self,client):
        self.client = client
    
    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member:nextcord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'User {member} has been kicked')

    @kick.error
    async def kick_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You dont have permission to kick people!")

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member:nextcord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'User {member} has been banned!')

    @ban.error
    async def ban_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have permissions to ban people!")
    
    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def add_role(self, ctx, user: nextcord.Member,*, role: nextcord.Role):

        if role in user.roles:
            await ctx.send(f'{user.mention} already has the role, {role}')
        else:
            await user.add_roles(role)
            await ctx.send(f'Added {role} to {user.mention}!')
    
    @add_role.error
    async def add_role_error(self, ctx, error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command!")

    @commands.command()
    @commands.has_permissions(manage_roles = True)
    async def remove_role(self, ctx, user: nextcord.Member,*, role: nextcord.Role):

        if role in user.roles:
            await user.remove_roles(role)
            await ctx.send(f'Removed {role} from {user.mention}!')
        else:
            await ctx.send(f'{user.mention} does not have the role {role}!')
    
    @remove_role.error
    async def remove_role_error(self, ctx, error):
        if isinstance(error,commands.MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


def setup(client):
    client.add_cog(Admin(client))