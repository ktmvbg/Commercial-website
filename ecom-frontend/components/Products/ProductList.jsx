/* eslint-disable @next/next/no-img-element */

import Image from "next/image";
import { getProducts } from "./product.api";
import { useEffect, useState } from "react";
import Link from "next/link";

export default function ProductList(props) {
  const products = props.products;
  return (
    <div className="bg-white">
      {/* <div className="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8"> */}
      <div className="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
        {products.map((product) => (
          <div key={product.id} className="group relative">
            <div className="aspect-h-1 aspect-w-1 overflow-hidden rounded-lg bg-gray-200 group-hover:opacity-75">
              <img
                src={product.imageSrc}
                alt={product.imageAlt}
                className="h-full w-full object-cover object-center"
              />
            </div>
            <div className="mt-4 flex justify-between">
              <div>
                <Link href={product.href}>
                  <h3 className="text-sm text-gray-700">
                    <span aria-hidden="true" className="absolute inset-0" />
                    {product.name}
                  </h3>
                </Link>

                <p className="mt-1 text-sm text-gray-500">
                  {product.description}
                </p>
              </div>
              <p className="text-sm font-medium text-gray-900">
                {product.price}
              </p>
            </div>
          </div>
        ))}
      </div>
    </div>
    // </div>
  );
}
