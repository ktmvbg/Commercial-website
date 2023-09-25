import FloatActionButton from "../buttons/FloatActionButton";
import ChatButton from "components/buttons/ChatButton";
import { Theme } from "@radix-ui/themes";
import Footer from "components/layouts/Footer";
// import Navigation from 'components/layouts/Navigation';
import dynamic from "next/dynamic";
import { CartProvider } from "hooks/CartContext";

const Navigation = dynamic(() => import("components/layouts/Navigation"), {
  ssr: false,
});
export default function NormalLayout({ children }) {
  return (
    <CartProvider>
      <div className="bg-white h-full">
        <Navigation />
        {children}
        <ChatButton />
        <Footer />
      </div>
    </CartProvider>
  );
}
