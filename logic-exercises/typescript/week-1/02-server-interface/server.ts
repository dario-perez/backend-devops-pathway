export interface Server {
  id: number;
  hostname: string;
  status: 'online' | 'offline' | 'maintenance'
  tags: string[];
}