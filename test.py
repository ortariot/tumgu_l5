import asyncio

from db.roleservice import role_service


async def runner():


    res = await role_service.get_role(1)
    
    # res = await role_service.add_role(name="super", level=6)

    print(res)



if __name__ == "__main__":
   

   asyncio.run(runner())