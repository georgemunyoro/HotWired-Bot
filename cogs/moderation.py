import asyncio

import discord
from cogs.utils.embedHandler import failure, info, success
from discord.ext import Bot
from discord.ext.commands import (Cog, Context, bot_has_permissions, command,
                                  has_permissions)


class Moderation(Cog):
    """This cog provides moderation commands."""
    def __init__(self, bot: Bot) -> None:
        self.bot = bot

    @command()
    @bot_has_permissions(kick_members=True)
    @has_permissions(kick_members=True)
    async def kick(self, ctx: Context, member: discord.Member, *, reason: str = "N/A") -> None:
        """Kick a User."""
        embed = discord.Embed(title="Infraction information", color=discord.Color.red())
        embed.add_field(name="Type", value="Kick")
        embed.add_field(name="Reason", value=reason)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name=member.name, url=member.avatar_url)
        embed.set_footer(text=member.guild.name, icon_url=member.guild.icon_url)

        await ctx.send(embed=embed)
        await member.send(embed=embed)
        await member.kick(reason=reason)

    @command()
    @bot_has_permissions(ban_members=True)
    @has_permissions(ban_members=True)
    async def ban(self, ctx: Context, member: discord.Member, *, reason: str = "No Reason Stated.") -> None:
        """Ban a User."""
        embed = discord.Embed(title="Infraction information", color=discord.Color.red())
        embed.add_field(name="Type", value="Ban")
        embed.add_field(name="Reason", value=reason)
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_author(name=member.name, url=member.avatar_url)
        embed.set_footer(text=member.guild.name, icon_url=member.guild.icon_url)

        await ctx.send(embed=embed)
        await member.send(embed=embed)
        await member.ban(reason=reason)

    @command()
    @bot_has_permissions(ban_members=True)
    @has_permissions(ban_members=True)
    async def unban(ctx: Context, *, member: str) -> None:
        """Unban a User."""
        # TODO: Use custom converter for `member`
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        # TODO: There might be a better way to handle this
        for ban_entry in banned_users:
            user = ban_entry.user

            if(user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'Unbanned **{user.name}#{user.discriminator}**')
                return

    @command()
    @bot_has_permissions(manage_messages=True)
    @has_permissions(manage_messages=True)
    async def clear(self, ctx: Context, amount: int) -> None:
        """Clear specified number of messages."""

        # TODO: Check if this condition is necessary
        if amount is not None:
            await ctx.channel.purge(limit=amount+1)
            await ctx.send('**Messages cleared** ' + ctx.message.author.mention)
            await asyncio.sleep(2.5)
            await ctx.channel.purge(limit=1)
        else:
            await ctx.send('please specify the number of messages to clear')

    @command()
    @bot_has_permissions(manage_roles=True)
    @has_permissions(manage_roles=True, manage_messages=True)
    async def promote(self, ctx: Context, member: discord.Member, role: discord.Role) -> None:
        """Promote member to role."""
        # TODO: A custom check can handle this
        if role >= ctx.author.top_role:
            await ctx.send(embed=failure("Role needs to be below you in hierarchy."))
            return
        if role in member.roles:
            await ctx.send(embed=failure(f"{member.mention} already has role {role.mention}!"))
            return

        await member.add_roles(role)

        await ctx.send(embed=success(f"{member.mention} is promoted to {role.mention}", ctx.me), delete_after=5)

        dm_embed = info(
            (
                f"You are now promoted to role **{role.name}** in our community.\n"
                "`'With great power comes great responsibility'`\n"
                "Be active and keep the community safe."
            ),
            ctx.me,
            "Congratulations!"
        )

        dm_embed.set_footer(text="Promotion Command.")
        await member.send(embed=dm_embed)


def setup(bot: Bot) -> None:
    bot.add_cog(Moderation(bot))
