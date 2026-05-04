"use client";

import { useAuth } from "@/context/AuthContext";
import { usePathname, useRouter } from "next/navigation";
import { useEffect, useState } from "react";
import Sidebar from "./Sidebar";

// Pages that DON'T require login
const PUBLIC_ROUTES = ["/", "/login"];

export default function AuthGuard({ children }: { children: React.ReactNode }) {
  const { user, loading } = useAuth();
  const pathname = usePathname();
  const router = useRouter();
  const [isRedirecting, setIsRedirecting] = useState(false);

  const isPublicRoute = PUBLIC_ROUTES.includes(pathname);
  const isLoginPage = pathname === "/login";

  useEffect(() => {
    if (loading) return;

    // Logged-in user on login page → send them to skill input first
    if (user && isLoginPage) {
      setIsRedirecting(true);
      router.replace("/skill-input");
      return;
    }

    // Not logged in, on a protected route → send to login
    if (!user && !isPublicRoute) {
      setIsRedirecting(true);
      router.replace("/login");
      return;
    }

    // NEW LOGIC: Prevent accessing dashboard/roadmap without skill input
    if (user && (pathname === "/dashboard" || pathname === "/roadmap")) {
      const hasAnalysis = sessionStorage.getItem("skillforge_analysis");
      if (!hasAnalysis) {
        setIsRedirecting(true);
        router.replace("/skill-input");
        return;
      }
    }

    setIsRedirecting(false);
  }, [user, loading, isLoginPage, isPublicRoute, router, pathname]);

  // Show loading spinner while auth state is resolving or redirecting
  if (loading || isRedirecting) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-[#09090b]">
        <div className="flex flex-col items-center gap-4">
          <div className="h-10 w-10 animate-spin rounded-full border-3 border-zinc-700 border-t-teal-500" />
          <p className="text-sm text-zinc-500">Loading...</p>
        </div>
      </div>
    );
  }

  // Login page — no sidebar
  if (isLoginPage) {
    if (user) return null; // will redirect via useEffect
    return <>{children}</>;
  }

  // Home page (public landing) — no sidebar needed
  if (pathname === "/") {
    return <>{children}</>;
  }

  // Protected pages — require auth + sidebar
  if (!user) return null; // will redirect via useEffect

  return (
    <div className="flex flex-col lg:flex-row bg-[#09090b] min-h-screen">
      <Sidebar />
      <main className="flex-1 lg:ml-64 pb-20 lg:pb-0">{children}</main>
    </div>
  );
}
