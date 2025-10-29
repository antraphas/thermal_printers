import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  /* config options here */
  reactCompiler: true,
  async rewrites() {
    return [
      {
        source: '/Downloads/:path*',
        destination: '/api/download/:path*',
      },
    ];
  },
};

export default nextConfig;
