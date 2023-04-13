@client.command(aliases=['LoveTester'])
async def _Lovetester(ctx):
    loveResponses = ['Casanova',
                     'Hot tamale',
                     'Luke warm Luke',
                     'Lovelorn',
                     'Cold fish']
    await ctx.send(f'Your love level is {random.choice(loveResponses)}')