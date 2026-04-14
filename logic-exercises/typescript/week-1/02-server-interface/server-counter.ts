import type { Server } from './server'

const serverList: Server[] = [
  { id: 1, hostname: 'srv-01', status: 'online', tags: [] },
  { id: 2, hostname: 'srv-02', status: 'offline', tags: [] },
  { id: 3, hostname: 'srv-03', status: 'offline', tags: [] },
  { id: 4, hostname: 'srv-04', status: 'online', tags: [] },
]

function countOnlineServers(servers: Server[]): number {
  const onlineServers = servers.filter(s => s.status === 'online').length
  return onlineServers
}

console.log(`Total servers online: ${countOnlineServers(serverList)}`);