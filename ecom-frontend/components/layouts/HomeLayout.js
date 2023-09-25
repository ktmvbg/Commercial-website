import FloatActionButton from "../buttons/FloatActionButton";
import ChatButton from "components/buttons/ChatButton";
import { Theme } from "@radix-ui/themes";
import Footer from "components/layouts/HomeFooter";
// import Navigation from 'components/layouts/HomeNavigation';
import dynamic from "next/dynamic";
import { CartProvider } from "hooks/CartContext";

const Navigation = dynamic(() => import("components/layouts/HomeNavigation"), {
  ssr: false,
});

export default function HomeLayout({ children }) {
  return (
    <CartProvider>
      <div className="bg-white">
        <Navigation />
        {children}
        <ChatButton />
        <Footer />
      </div>
    </CartProvider>
  );
}
