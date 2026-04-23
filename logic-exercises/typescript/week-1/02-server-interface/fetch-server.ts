import type { Server } from "./server";

function getServerById(id: number): Promise<Server>{
  return new Promise((resolve) => {
    setTimeout(() => {
      const mockServer: Server = {
        id: id,
        hostname: 'main-db-server',
        status: 'online',
        tags: ['production', 'database'],
      }

      resolve(mockServer)
    }, 2000);
  });
}

async function runLogic() {
  console.log('Fetching server data...');
  const result = await getServerById(1);
  console.log('Server found:', result.hostname);
  return result;
}

runLogic()