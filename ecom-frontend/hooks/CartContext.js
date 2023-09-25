import { createContext, useEffect, useState } from "react";
import useAuth from "./useAuth";
import config from "components/config";

export const CartContext = createContext();

export const CartProvider = ({ children }) => {
  const auth = useAuth();

  const [cartItems, setCartItems] = useState(
    typeof window === "undefined"
      ? []
      : JSON.parse(localStorage.getItem("cartItems")) || []
  );

  function updateCart() {
    const url = config.API + "/api/cart";
    if (auth.isLogged) {
      return fetch(url, {
        headers: {
          Authorization: `Bearer ${auth.token}`,
        },
      })
        .then((res) => res.json())
        .then((res) => {
          setCartItems(res);
          localStorage.setItem("cartItems", JSON.stringify(res));
        });
    }
  }

  function addToCart(product_id, quantity = 1) {
    if (!auth.isLogged) {
      return;
    }
    const url = config.API + "/api/cart";
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${auth.token}`,
      },
      body: JSON.stringify({ product_id, quantity }),
    }).then((res) => res.json());
    updateCart();
  }

  function removeFromCart(product_id) {
    if (!auth.isLogged) {
      return;
    }
    const url = config.API + "/api/cart";
    fetch(url, {
      method: "DELETE",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${auth.token}`,
      },
      body: JSON.stringify({ product_id: product_id }),
    }).then((res) => res.json());
    updateCart();
  }

  function updateProductQuantity(product_id, quantity) {
    if (!auth.isLogged) {
      return;
    }
    const url = config.API + "/api/cart";
    fetch(url, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${auth.token}`,
      },
      body: JSON.stringify({ product_id, quantity }),
    }).then((res) => res.json());
    updateCart();
  }

  const getCartTotal = () => {
    return cartItems.reduce(
      (total, item) => total + item.price * item.quantity,
      0
    );
  };

  const getCartTotalQuantity = () => {
    return cartItems.reduce((total, item) => total + item.quantity, 0);
  };

  const clearCart = () => {
    if (!auth.isLogged) {
      return;
    }
    const url = config.API + "/api/cart/clear";
    fetch(url, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${auth.token}`,
      },
    }).then((res) => res.json());
    updateCart();
  };

  useEffect(() => {
    updateCart();
  }, []);

  useEffect(() => {
    localStorage.setItem("cartItems", JSON.stringify(cartItems));
  }, [cartItems]); // Include cartItems as a dependency here

  return (
    <CartContext.Provider
      value={{
        cartItems,
        setCartItems,
        addToCart,
        removeFromCart,
        updateProductQuantity,
        getCartTotal,
        getCartTotalQuantity,
        clearCart,
      }}
    >
      {children}
    </CartContext.Provider>
  );
};
